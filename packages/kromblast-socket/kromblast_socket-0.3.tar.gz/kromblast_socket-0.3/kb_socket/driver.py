from socket import socket, AF_INET, SOCK_STREAM


class Driver:
    host: str
    port: int
    sock: socket

    is_connected: bool = False

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(1)
        self.is_connected = True

    def send(self, data: bytes) -> None:
        self.sock.send(data + b'\0')

    def recv(self) -> bytes:
        data = b''
        while True:
            get = self.sock.recv(1)
            if not get:
                break
            if get == b'\x00':
                break
            data += get
        return data

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        if not self.is_connected:
            return
        self.is_connected = False
        self.sock.close()
