from typing import Tuple, Callable
from .kb_socket import KbSocket, Promise


class DefaultKbSocket(KbSocket):
    mode: str = "promised"

    MODE_PROMISED: str = "promised"
    MODE_SYNC: str = "sync"

    def __init__(self, host: str, port: int, mode: str = "promised") -> None:
        super().__init__(host, port)
        self.mode = mode

    def send_default(self, player: str, channel: str,
                     message: str) -> Promise | Tuple[str, str]:
        if self.mode == self.MODE_PROMISED:
            return self.send_promised(player, channel, message)
        elif self.mode == self.MODE_SYNC:
            return self.send_sync(player, channel, message)
        else:
            raise ValueError("Mode not supported")

    def listen_signal(self, channel: str,
                      callback: Callable[[str, str], None]) -> None:
        self.send("_socket_control", "listen", channel, callback, False)

    # def unlisten_signal(self, channel: str) -> None:
    #     self.runner.send("_socket_control", "unlisten", channel, None, False)

    def execute(self, code: str) -> Promise | Tuple[str, str]:
        return self.send_default("_socket_control", "execute", code)

    def send_signal(self, channel: str,
                    message: str) -> Promise | Tuple[str, str]:
        self.send("_dispatcher", channel, message)

    def navigate(self, path: str) -> Promise | Tuple[str, str]:
        self.send("_kromblast", "navigate", path)

    def init_inject(self, code: str) -> Promise | Tuple[str, str]:
        self.send("_kromblast", "init_inject", code)

    def inject(self, code: str) -> Promise | Tuple[str, str]:
        self.send("_kromblast", "inject", code)
