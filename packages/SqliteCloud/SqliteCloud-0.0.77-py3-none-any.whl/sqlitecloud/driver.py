import logging
import select
import socket
import ssl
import threading
from io import BufferedReader, BufferedWriter
from typing import Callable, Optional, Union

import lz4.block

from sqlitecloud.resultset import SQCloudResult, SqliteCloudResultSet
from sqlitecloud.types import (
    SQCLOUD_CMD,
    SQCLOUD_DEFAULT,
    SQCLOUD_INTERNAL_ERRCODE,
    SQCLOUD_RESULT_TYPE,
    SQCLOUD_ROWSET,
    SQCloudConfig,
    SQCloudConnect,
    SQCloudException,
    SQCloudNumber,
    SQCloudRowsetSignature,
    SQCloudValue,
)


class Driver:
    SQCLOUD_DEFAULT_UPLOAD_SIZE = 512 * 1024

    def __init__(self) -> None:
        # Used while parsing chunked rowset
        self._rowset: SQCloudResult = None

    def connect(
        self, hostname: str, port: int, config: SQCloudConfig
    ) -> SQCloudConnect:
        """
        Connect to the SQLite Cloud server.

        Args:
            hostname (str): The hostname of the server.
            port (int): The port number of the server.
            config (SQCloudConfig): The configuration for the connection.

        Returns:
            SQCloudConnect: The connection object.

        Raises:
            SQCloudException: If an error occurs while connecting the socket.
        """
        sock = self._internal_connect(hostname, port, config)

        connection = SQCloudConnect()
        connection.config = config
        connection.socket = sock

        self._internal_config_apply(connection, config)

        return connection

    def disconnect(self, conn: SQCloudConnect, only_main_socket: bool = False) -> None:
        """
        Disconnect from the SQLite Cloud server.
        """
        try:
            if conn.socket:
                conn.socket.close()
            if not only_main_socket and conn.pubsub_socket:
                conn.pubsub_socket.close()
        finally:
            conn.socket = None
            if not only_main_socket:
                conn.pubsub_socket = None

    def execute(self, command: str, connection: SQCloudConnect) -> SQCloudResult:
        """
        Execute a query on the SQLite Cloud server.
        """
        return self._internal_run_command(connection, command)

    def send_blob(self, blob: bytes, conn: SQCloudConnect) -> SQCloudResult:
        """
        Send a blob to the SQLite Cloud server.
        """
        try:
            conn.isblob = True
            return self._internal_run_command(conn, blob)
        finally:
            conn.isblob = False

    def is_connected(
        self, connection: SQCloudConnect, main_socket: bool = True
    ) -> bool:
        """
        Check if the connection is still open.
        """
        sock = connection.socket if main_socket else connection.pubsub_socket

        if not sock:
            return False
        try:
            sock.sendall(b"")
        except OSError:
            return False

        return True

    def _internal_connect(
        self, hostname: str, port: int, config: SQCloudConfig
    ) -> socket:
        """
        Create a socket connection to the SQLite Cloud server.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(config.connect_timeout)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        if not config.insecure:
            context = ssl.create_default_context(cafile=config.root_certificate)
            if config.certificate:
                context.load_cert_chain(
                    certfile=config.certificate, keyfile=config.certificate_key
                )
            if config.no_verify_certificate:
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE

            sock = context.wrap_socket(sock, server_hostname=hostname)

        try:
            sock.connect((hostname, port))
        except Exception as e:
            errmsg = "An error occurred while initializing the socket."
            raise SQCloudException(errmsg) from e

        return sock

    def _internal_reconnect(self, buffer: bytes) -> bool:
        return True

    def _internal_setup_pubsub(self, connection: SQCloudConnect, buffer: bytes) -> bool:
        """
        Prepare the connection for PubSub.
        Opens a new specific socket and starts the thread to listen for incoming messages.
        """
        if self.is_connected(connection, False):
            return True

        if connection.pubsub_callback is None:
            raise SQCloudException(
                "A callback function must be provided to setup the PubSub connection."
            )

        connection.pubsub_socket = self._internal_connect(
            connection.config.account.hostname,
            connection.config.account.port,
            connection.config,
        )

        self._internal_run_command(connection, buffer, False)
        thread = threading.Thread(
            target=self._internal_pubsub_thread, args=(connection,)
        )
        # kill the thread when the main one is terminated
        thread.daemon = True
        thread.start()
        connection.pubsub_thread = thread

        return True

    def _internal_pubsub_thread(self, connection: SQCloudConnect) -> None:
        blen = 2048
        buffer: bytes = b""

        try:
            while True:
                tread = 0

                try:
                    if not connection.pubsub_socket:
                        logging.info("PubSub socket dismissed.")
                        break

                    # wait for the socket to be readable (no timeout)
                    ready_to_read, _, errors = select.select(
                        [connection.pubsub_socket], [], []
                    )
                    # eg, if the socket is closed
                    if len(errors) > 0:
                        break
                    # eg, no data to read
                    if len(ready_to_read) == 0:
                        continue

                    data = connection.pubsub_socket.recv(blen)
                    if not data:
                        logging.info("PubSub connection closed.")
                        break
                except Exception as e:
                    logging.error(
                        f"An error occurred while reading data: {SQCLOUD_INTERNAL_ERRCODE.NETWORK.value} ({e})."
                    )
                    break

                nread = len(data)
                tread += nread
                blen -= nread
                buffer += data

                sqcloud_number = self._internal_parse_number(buffer)
                clen = sqcloud_number.value
                if clen == 0:
                    continue

                # check if read is complete
                # clen is the lenght parsed in the buffer
                # cstart is the index of the first space
                cstart = sqcloud_number.cstart
                if clen + cstart != tread:
                    continue

                result = self._internal_parse_buffer(connection, buffer, tread)
                if result.tag == SQCLOUD_RESULT_TYPE.RESULT_STRING:
                    result.tag = SQCLOUD_RESULT_TYPE.RESULT_JSON

                connection.pubsub_callback(
                    connection, SqliteCloudResultSet(result), connection.pubsub_data
                )
        except Exception as e:
            logging.error(f"An error occurred while parsing data: {e}.")

        finally:
            connection.pubsub_callback(connection, None, connection.pubsub_data)

    def upload_database(
        self,
        connection: SQCloudConnect,
        dbname: str,
        key: Optional[str],
        is_file_transfer: bool,
        snapshot_id: int,
        is_internal_db: bool,
        fd: BufferedReader,
        dbsize: int,
        xCallback: Callable[[BufferedReader, int, int, int], bytes],
    ) -> None:
        """
        Uploads a database to the server.

        Args:
            connection (SQCloudConnect): The connection object to the SQLite Cloud server.
            dbname (str): The name of the database to upload.
            key (Optional[str]): The encryption key for the database, if applicable.
            is_file_transfer (bool): Indicates whether the database is being transferred as a file.
            snapshot_id (int): The ID of the snapshot to upload.
            is_internal_db (bool): Indicates whether the database is an internal database.
            fd (BufferedReader): The file descriptor of the database file.
            dbsize (int): The size of the database file.
            xCallback (Callable[[BufferedReader, int, int, int], bytes]): The callback function to read the buffer.

        Raises:
            SQCloudException: If an error occurs during the upload process.

        """
        keyarg = "KEY " if key else ""
        keyvalue = key if key else ""

        # prepare command to execute
        command = ""
        if is_file_transfer:
            internalarg = "INTERNAL" if is_internal_db else ""
            command = f"TRANSFER DATABASE '{dbname}' {keyarg}{keyvalue} SNAPSHOT {snapshot_id} {internalarg}"
        else:
            command = f"UPLOAD DATABASE '{dbname}' {keyarg}{keyvalue}"

        # execute command on server side
        result = self._internal_run_command(connection, command)
        if not result.data[0]:
            raise SQCloudException(
                "An error occurred while initializing the upload of the database."
            )

        buffer: bytes = b""
        blen = 0
        nprogress = 0
        try:
            while True:
                # execute callback to read buffer
                blen = SQCLOUD_DEFAULT.UPLOAD_SIZE.value
                try:
                    buffer = xCallback(fd, blen, dbsize, nprogress)
                    blen = len(buffer)
                except Exception as e:
                    raise SQCloudException(
                        "An error occurred while reading the file."
                    ) from e

                try:
                    # send also the final confirmation blob of zero bytes
                    self.send_blob(buffer, connection)
                except Exception as e:
                    raise SQCloudException(
                        "An error occurred while uploading the file."
                    ) from e

                # update progress
                nprogress += blen

                if blen == 0:
                    # Upload completed
                    break
        except Exception as e:
            self._internal_run_command(connection, "UPLOAD ABORT")
            raise e

    def download_database(
        self,
        connection: SQCloudConnect,
        dbname: str,
        fd: BufferedWriter,
        xCallback: Callable[[BufferedWriter, int, int, int], bytes],
        if_exists: bool,
    ) -> None:
        """
        Downloads a database from the SQLite Cloud service.

        Args:
            connection (SQCloudConnect): The connection object used to communicate with the SQLite Cloud service.
            dbname (str): The name of the database to download.
            fd (BufferedWriter): The file descriptor to write the downloaded data to.
            xCallback (Callable[[BufferedWriter, int, int, int], bytes]): A callback function to write downloaded data with the download progress information.
            if_exists (bool): If True, the download won't rise an exception if database is missing.

        Raises:
            SQCloudException: If an error occurs while downloading the database.

        """
        exists_cmd = " IF EXISTS" if if_exists else ""
        result = self._internal_run_command(
            connection, f"DOWNLOAD DATABASE {dbname}{exists_cmd};"
        )

        if result.nrows == 0:
            raise SQCloudException(
                "An error occurred while initializing the download of the database."
            )

        # result is an ARRAY (database size, number of pages, raft_index)
        download_info = result.data[0]
        db_size = int(download_info[0])

        # loop to download
        progress_size = 0

        try:
            while progress_size < db_size:
                result = self._internal_run_command(connection, "DOWNLOAD STEP")

                # res is BLOB, decode it
                data = result.data[0]
                data_len = len(data)

                # execute callback (with progress_size updated)
                progress_size += data_len
                xCallback(fd, data, data_len, db_size, progress_size)

                # check exit condition
                if data_len == 0:
                    break
        except Exception as e:
            self._internal_run_command(connection, "DOWNLOAD ABORT")
            raise e

    def _internal_config_apply(
        self, connection: SQCloudConnect, config: SQCloudConfig
    ) -> None:
        if config.timeout > 0:
            connection.socket.settimeout(config.timeout)

        buffer = ""

        if config.account.apikey:
            buffer += f"AUTH APIKEY {config.account.apikey};"

        if config.account.username and config.account.password:
            command = "HASH" if config.account.password_hashed else "PASSWORD"
            buffer += f"AUTH USER {config.account.username} {command} {config.account.password};"

        if config.account.dbname:
            if config.create and not config.memory:
                buffer += f"CREATE DATABASE {config.account.dbname} IF NOT EXISTS;"
            buffer += f"USE DATABASE {config.account.dbname};"

        if config.compression:
            buffer += "SET CLIENT KEY COMPRESSION TO 1;"

        if config.zerotext:
            buffer += "SET CLIENT KEY ZEROTEXT TO 1;"

        if config.non_linearizable:
            buffer += "SET CLIENT KEY NONLINEARIZABLE TO 1;"

        if config.noblob:
            buffer += "SET CLIENT KEY NOBLOB TO 1;"

        if config.maxdata:
            buffer += f"SET CLIENT KEY MAXDATA TO {config.maxdata};"

        if config.maxrows:
            buffer += f"SET CLIENT KEY MAXROWS TO {config.maxrows};"

        if config.maxrowset:
            buffer += f"SET CLIENT KEY MAXROWSET TO {config.maxrowset};"

        if len(buffer) > 0:
            self._internal_run_command(connection, buffer)

    def _internal_run_command(
        self,
        connection: SQCloudConnect,
        command: Union[str, bytes],
        main_socket: bool = True,
    ) -> SQCloudResult:
        self._internal_socket_write(connection, command, main_socket)
        return self._internal_socket_read(connection, main_socket)

    def _internal_socket_write(
        self,
        connection: SQCloudConnect,
        command: Union[str, bytes],
        main_socket: bool = True,
    ) -> None:
        # compute header
        delimit = "$" if connection.isblob else "+"
        buffer = command.encode() if isinstance(command, str) else command
        buffer_len = len(buffer)
        header = f"{delimit}{buffer_len} "

        sock = connection.socket if main_socket else connection.pubsub_socket

        # write header
        try:
            sock.sendall(header.encode())
        except Exception as exc:
            raise SQCloudException(
                "An error occurred while writing header data.",
                SQCLOUD_INTERNAL_ERRCODE.NETWORK,
            ) from exc

        # write buffer
        if buffer_len == 0:
            return
        try:
            sock.sendall(buffer)
        except Exception as exc:
            raise SQCloudException(
                "An error occurred while writing data.",
                SQCLOUD_INTERNAL_ERRCODE.NETWORK,
            ) from exc

    def _internal_socket_read(
        self, connection: SQCloudConnect, main_socket: bool = True
    ) -> SQCloudResult:
        """
        Read from the socket and parse the response.

        The buffer is stored as a string of bytes without decoding it with UTF-8.
        The dimensions (LEN) specified in the SCSP protocol are in bytes, while
        Python counts decoded strings in characters. This can cause issues when
        slicing the buffer into parts if there are special characters like "ò".
        """
        buffer = b""
        buffer_size = 8192
        nread = 0

        sock = connection.socket if main_socket else connection.pubsub_socket

        while True:
            try:
                data = sock.recv(buffer_size)
                if not data:
                    raise SQCloudException("Incomplete response from server.")
            except Exception as exc:
                raise SQCloudException(
                    "An error occurred while reading data from the socket.",
                    SQCLOUD_INTERNAL_ERRCODE.NETWORK,
                ) from exc

            # the expected data length to read
            # matches the string size before decoding it
            nread += len(data)
            # update buffers
            buffer += data

            c = chr(buffer[0])

            if (
                c == SQCLOUD_CMD.INT.value
                or c == SQCLOUD_CMD.FLOAT.value
                or c == SQCLOUD_CMD.NULL.value
            ):
                if not buffer.endswith(b" "):
                    continue
            elif c == SQCLOUD_CMD.ROWSET_CHUNK.value:
                isEndOfChunk = buffer.endswith(SQCLOUD_ROWSET.CHUNKS_END.value)
                if not isEndOfChunk:
                    continue
            else:
                sqcloud_number = self._internal_parse_number(buffer)
                n = sqcloud_number.value
                cstart = sqcloud_number.cstart

                can_be_zerolength = (
                    c == SQCLOUD_CMD.BLOB.value or c == SQCLOUD_CMD.STRING.value
                )
                if n == 0 and not can_be_zerolength:
                    continue
                if n + cstart != nread:
                    continue

            return self._internal_parse_buffer(connection, buffer, len(buffer))

    def _internal_parse_number(self, buffer: bytes, index: int = 1) -> SQCloudNumber:
        sqcloud_number = SQCloudNumber()
        sqcloud_number.value = 0
        extvalue = 0
        isext = False
        blen = len(buffer)

        # from 1 to skip the first command type character
        for i in range(index, blen):
            c = chr(buffer[i])

            # check for optional extended error code (ERRCODE:EXTERRCODE)
            if c == ":":
                isext = True
                continue

            # check for end of value
            if c == " ":
                sqcloud_number.cstart = i + 1
                sqcloud_number.extcode = extvalue
                return sqcloud_number

            val = int(c) if c.isdigit() else 0

            # compute numeric value
            if isext:
                extvalue = (extvalue * 10) + val
            else:
                sqcloud_number.value = (sqcloud_number.value * 10) + val

        sqcloud_number.value = 0
        return sqcloud_number

    def _internal_parse_buffer(
        self, connection: SQCloudConnect, buffer: bytes, blen: int
    ) -> SQCloudResult:
        # possible return values:
        # True 	=> OK
        # False 	=> error
        # integer
        # double
        # string
        # list
        # object
        # None

        # check OK value
        if buffer == b"+2 OK":
            return SQCloudResult(SQCLOUD_RESULT_TYPE.RESULT_OK, True)

        cmd = chr(buffer[0])

        # check for compressed result
        if cmd == SQCLOUD_CMD.COMPRESSED.value:
            buffer = self._internal_uncompress_data(buffer)
            if buffer is None:
                raise SQCloudException(
                    f"An error occurred while decompressing the input buffer of len {blen}."
                )

            # buffer after decompression
            blen = len(buffer)
            cmd = chr(buffer[0])

        # first character contains command type
        if cmd in [
            SQCLOUD_CMD.ZEROSTRING.value,
            SQCLOUD_CMD.RECONNECT.value,
            SQCLOUD_CMD.PUBSUB.value,
            SQCLOUD_CMD.COMMAND.value,
            SQCLOUD_CMD.STRING.value,
            SQCLOUD_CMD.ARRAY.value,
            SQCLOUD_CMD.BLOB.value,
            SQCLOUD_CMD.JSON.value,
        ]:
            sqlite_number = self._internal_parse_number(buffer)
            len_ = sqlite_number.value
            cstart = sqlite_number.cstart
            if len_ == 0:
                return SQCloudResult(SQCLOUD_RESULT_TYPE.RESULT_STRING, "")

            tag = (
                SQCLOUD_RESULT_TYPE.RESULT_JSON
                if cmd == SQCLOUD_CMD.JSON.value
                else SQCLOUD_RESULT_TYPE.RESULT_STRING
            )

            if cmd == SQCLOUD_CMD.ZEROSTRING.value:
                len_ -= 1
            clone = buffer[cstart : cstart + len_]

            if cmd == SQCLOUD_CMD.COMMAND.value:
                return self._internal_run_command(connection, clone)
            elif cmd == SQCLOUD_CMD.PUBSUB.value:
                return SQCloudResult(
                    SQCLOUD_RESULT_TYPE.RESULT_OK,
                    self._internal_setup_pubsub(connection, clone),
                )
            elif cmd == SQCLOUD_CMD.RECONNECT.value:
                return SQCloudResult(
                    SQCLOUD_RESULT_TYPE.RESULT_OK, self._internal_reconnect(clone)
                )
            elif cmd == SQCLOUD_CMD.ARRAY.value:
                return SQCloudResult(
                    SQCLOUD_RESULT_TYPE.RESULT_ARRAY, self._internal_parse_array(clone)
                )
            elif cmd == SQCLOUD_CMD.BLOB.value:
                tag = SQCLOUD_RESULT_TYPE.RESULT_BLOB

            clone = clone.decode() if cmd != SQCLOUD_CMD.BLOB.value else clone
            return SQCloudResult(tag, clone)

        elif cmd == SQCLOUD_CMD.ERROR.value:
            # -LEN ERRCODE:EXTCODE ERRMSG
            sqlite_number = self._internal_parse_number(buffer)
            len_ = sqlite_number.value
            cstart = sqlite_number.cstart
            clone = buffer[cstart:]

            sqlite_number = self._internal_parse_number(clone, 0)
            cstart2 = sqlite_number.cstart

            errcode = sqlite_number.value
            xerrcode = sqlite_number.extcode

            len_ -= cstart2
            errmsg = clone[cstart2:]

            raise SQCloudException(errmsg.decode(), errcode, xerrcode)

        elif cmd in [SQCLOUD_CMD.ROWSET.value, SQCLOUD_CMD.ROWSET_CHUNK.value]:
            # CMD_ROWSET:          *LEN 0:VERSION ROWS COLS DATA
            # - When decompressed, LEN for ROWSET is *0
            #
            # CMD_ROWSET_CHUNK:    /LEN IDX:VERSION ROWS COLS DATA
            #
            rowset_signature = self._internal_parse_rowset_signature(buffer)
            if rowset_signature.start < 0:
                raise SQCloudException("Cannot parse rowset signature")

            # check for end-of-chunk condition
            if rowset_signature.start == 0 and rowset_signature.version == 0:
                rowset = self._rowset
                self._rowset = None
                return rowset

            rowset = self._internal_parse_rowset(
                buffer,
                rowset_signature.start,
                rowset_signature.idx,
                rowset_signature.version,
                rowset_signature.nrows,
                rowset_signature.ncols,
            )

            # continue parsing next chunk in the buffer
            sign_len = rowset_signature.len
            buffer = buffer[sign_len + len(f"/{sign_len} ") :]
            if cmd == SQCLOUD_CMD.ROWSET_CHUNK.value and buffer:
                return self._internal_parse_buffer(connection, buffer, len(buffer))

            return rowset

        elif cmd == SQCLOUD_CMD.NULL.value:
            return SQCloudResult(SQCLOUD_RESULT_TYPE.RESULT_NONE, None)

        elif cmd in [SQCLOUD_CMD.INT.value, SQCLOUD_CMD.FLOAT.value]:
            sqcloud_value = self._internal_parse_value(buffer)
            clone = sqcloud_value.value

            tag = (
                SQCLOUD_RESULT_TYPE.RESULT_INTEGER
                if cmd == SQCLOUD_CMD.INT.value
                else SQCLOUD_RESULT_TYPE.RESULT_FLOAT
            )

            if clone is None:
                return SQCloudResult(tag, 0)

            if cmd == SQCLOUD_CMD.INT.value:
                return SQCloudResult(tag, int(clone))
            return SQCloudResult(tag, float(clone))

        elif cmd == SQCLOUD_CMD.RAWJSON.value:
            return SQCloudResult(SQCLOUD_RESULT_TYPE.RESULT_NONE, None)

        return SQCloudResult(SQCLOUD_RESULT_TYPE.RESULT_NONE, None)

    def _internal_uncompress_data(self, buffer: bytes) -> Optional[bytes]:
        """
        %LEN COMPRESSED UNCOMPRESSED BUFFER

        Args:
            buffer (str): The compressed data buffer.
            blen (int): The length of the buffer.

        Returns:
            str: The uncompressed data.
        """
        space_index = buffer.index(b" ")
        buffer = buffer[space_index + 1 :]

        # extract compressed size
        space_index = buffer.index(b" ")
        compressed_size = int(buffer[:space_index].decode("utf-8"))
        buffer = buffer[space_index + 1 :]

        # extract decompressed size
        space_index = buffer.index(b" ")
        uncompressed_size = int(buffer[:space_index].decode("utf-8"))
        buffer = buffer[space_index + 1 :]

        # extract data header
        header = buffer[:-compressed_size]

        # extract compressed data
        compressed_buffer = buffer[-compressed_size:]

        decompressed_buffer = header + lz4.block.decompress(
            compressed_buffer, uncompressed_size
        )

        # sanity check result
        if len(decompressed_buffer) != uncompressed_size + len(header):
            return None

        return decompressed_buffer

    def _internal_parse_array(self, buffer: bytes) -> list:
        start = 0
        sqlite_number = self._internal_parse_number(buffer, start)
        n = sqlite_number.value
        start = sqlite_number.cstart

        r: str = []
        for i in range(n):
            sqcloud_value = self._internal_parse_value(buffer, start)
            start += sqcloud_value.cellsize
            r.append(sqcloud_value.value)

        return r

    def _internal_parse_value(self, buffer: bytes, index: int = 0) -> SQCloudValue:
        sqcloud_value = SQCloudValue()
        len = 0
        cellsize = 0

        # handle special NULL value case
        c = chr(buffer[index])
        if buffer is None or c == SQCLOUD_CMD.NULL.value:
            len = 0
            if cellsize is not None:
                cellsize = 2

            sqcloud_value.len = len
            sqcloud_value.cellsize = cellsize

            return sqcloud_value

        sqcloud_number = self._internal_parse_number(buffer, index + 1)
        blen = sqcloud_number.value
        cstart = sqcloud_number.cstart

        # handle decimal/float cases
        if c == SQCLOUD_CMD.INT.value or c == SQCLOUD_CMD.FLOAT.value:
            nlen = cstart - index
            len = nlen - 2
            cellsize = nlen

            sqcloud_value.value = (buffer[index + 1 : index + 1 + len]).decode()
            sqcloud_value.len
            sqcloud_value.cellsize = cellsize

            return sqcloud_value

        len = blen - 1 if c == SQCLOUD_CMD.ZEROSTRING.value else blen
        cellsize = blen + cstart - index

        sqcloud_value.value = (buffer[cstart : cstart + len]).decode()
        sqcloud_value.len = len
        sqcloud_value.cellsize = cellsize

        return sqcloud_value

    def _internal_parse_rowset_signature(self, buffer: bytes) -> SQCloudRowsetSignature:
        # ROWSET:          *LEN 0:VERS NROWS NCOLS DATA
        # ROWSET in CHUNK: /LEN IDX:VERS NROWS NCOLS DATA

        signature = SQCloudRowsetSignature()

        # check for end-of-chunk condition
        if buffer == SQCLOUD_ROWSET.CHUNKS_END.value:
            signature.version = 0
            signature.start = 0
            return signature

        start = 1
        counter = 0
        n = len(buffer)
        for i in range(n):
            if chr(buffer[i]) != " ":
                continue
            counter += 1

            data = (buffer[start:i]).decode()
            start = i + 1

            if counter == 1:
                signature.len = int(data)
            elif counter == 2:
                # idx:vers
                values = data.split(":")
                signature.idx = int(values[0])
                signature.version = int(values[1])
            elif counter == 3:
                signature.nrows = int(data)
            elif counter == 4:
                signature.ncols = int(data)

                signature.start = start

                return signature
            else:
                return SQCloudRowsetSignature()
        return SQCloudRowsetSignature()

    def _internal_parse_rowset(
        self, buffer: bytes, start: int, idx: int, version: int, nrows: int, ncols: int
    ) -> SQCloudResult:
        rowset = None
        n = start
        ischunk = chr(buffer[0]) == SQCLOUD_CMD.ROWSET_CHUNK.value

        # idx == 0 means first (and only) chunk for rowset
        # idx == 1 means first chunk for chunked rowset
        first_chunk = (ischunk and idx == 1) or (not ischunk and idx == 0)
        if first_chunk:
            rowset = SQCloudResult(SQCLOUD_RESULT_TYPE.RESULT_ROWSET)
            rowset.nrows = nrows
            rowset.ncols = ncols
            rowset.version = version
            rowset.data = []
            if ischunk:
                self._rowset = rowset
            n = self._internal_parse_rowset_header(rowset, buffer, start)
            if n <= 0:
                raise SQCloudException("Cannot parse rowset header")
        else:
            rowset = self._rowset
            rowset.nrows += nrows

        # parse values
        self._internal_parse_rowset_values(rowset, buffer, n, nrows * ncols)

        return rowset

    def _internal_parse_rowset_header(
        self, rowset: SQCloudResult, buffer: bytes, start: int
    ) -> int:
        ncols = rowset.ncols

        # parse column names
        rowset.colname = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            number_len = sqcloud_number.value
            cstart = sqcloud_number.cstart
            value = buffer[cstart : cstart + number_len]
            rowset.colname.append(value.decode())
            start = cstart + number_len

        if rowset.version == 1:
            return start

        if rowset.version != 2:
            raise SQCloudException(f"Rowset version {rowset.version} is not supported.")

        # parse declared types
        rowset.decltype = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            number_len = sqcloud_number.value
            cstart = sqcloud_number.cstart
            value = buffer[cstart : cstart + number_len]
            rowset.decltype.append(value.decode())
            start = cstart + number_len

        # parse database names
        rowset.dbname = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            number_len = sqcloud_number.value
            cstart = sqcloud_number.cstart
            value = buffer[cstart : cstart + number_len]
            rowset.dbname.append(value.decode())
            start = cstart + number_len

        # parse table names
        rowset.tblname = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            number_len = sqcloud_number.value
            cstart = sqcloud_number.cstart
            value = buffer[cstart : cstart + number_len]
            rowset.tblname.append(value.decode())
            start = cstart + number_len

        # parse column original names
        rowset.origname = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            number_len = sqcloud_number.value
            cstart = sqcloud_number.cstart
            value = buffer[cstart : cstart + number_len]
            rowset.origname.append(value.decode())
            start = cstart + number_len

        # parse not null flags
        rowset.notnull = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            rowset.notnull.append(sqcloud_number.value)
            start = sqcloud_number.cstart

        # parse primary key flags
        rowset.prikey = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            rowset.prikey.append(sqcloud_number.value)
            start = sqcloud_number.cstart

        # parse autoincrement flags
        rowset.autoinc = []
        for i in range(ncols):
            sqcloud_number = self._internal_parse_number(buffer, start)
            rowset.autoinc.append(sqcloud_number.value)
            start = sqcloud_number.cstart

        return start

    def _internal_parse_rowset_values(
        self, rowset: SQCloudResult, buffer: bytes, start: int, bound: int
    ):
        # loop to parse each individual value
        for i in range(bound):
            sqcloud_value = self._internal_parse_value(buffer, start)
            start += sqcloud_value.cellsize
            rowset.data.append(sqcloud_value.value)
