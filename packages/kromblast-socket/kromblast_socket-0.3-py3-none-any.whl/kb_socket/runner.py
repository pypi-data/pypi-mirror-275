from threading import Thread
from typing import Dict, Callable, Tuple
from .driver import Driver
from .kb_protocol import KbProtocol
from random import randint

callback = Callable[[str, str, str], None]


class Runner(Thread):
    driver: Driver
    protocol: KbProtocol
    promise: Dict[str, Tuple[bool, callback]] = {}
    running: bool = True

    def __init__(self, host: str, port: int) -> None:
        super().__init__(name="KbSocketRunner")
        self.driver = Driver(host, port)
        self.protocol = KbProtocol()

    def send(self, player: str, channel: str,
             message: str, callback: callback | None = None,
             is_callback_deleted: bool = True) -> str:
        tmp_id = str(randint(0, 1000))
        while tmp_id in self.promise.keys():
            tmp_id = str(randint(0, 1000))
        if callback:
            self.promise[tmp_id] = (is_callback_deleted, callback)
        data = self.protocol.build_message(player, tmp_id, channel, message)
        self.driver.send(data)
        return tmp_id

    def close(self) -> None:
        self.running = False
        self.driver.close()

    def run(self) -> None:
        while self.running:
            try:
                data = self.driver.recv()
            except OSError:
                continue
            if not data:
                continue
            type_data, tmp_id, message = self.protocol.parse_response(data)
            if tmp_id in self.promise.keys():
                self.promise[tmp_id][1](tmp_id, type_data, message)
                if self.promise[tmp_id][0]:
                    del self.promise[tmp_id]
        self.driver.close()
        print("Runner stopped")
