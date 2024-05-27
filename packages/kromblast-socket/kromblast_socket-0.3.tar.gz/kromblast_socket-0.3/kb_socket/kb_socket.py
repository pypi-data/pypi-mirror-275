from typing import Dict
from .runner import Runner, callback
from .kb_promise import Promise


class KbSocket:
    runner: Runner
    promised: Dict[str, Promise] = {}

    def __init__(self, host: str, port: int) -> None:
        self.runner = Runner(host, port)
        self.runner.start()

    def send(self, player: str, channel: str,
             message: str, callback: callback | None = None,
             is_callback_deleted: bool = True) -> str:
        return self.runner.send(player, channel, message, callback,
                                is_callback_deleted)

    def _get_response(self, tmp_id: str, type_data: str, message: str) -> None:
        if tmp_id in self.promised.keys():
            self.promised[tmp_id].resolve((type_data, message))
            print(f"promise resolved: {type_data} {tmp_id} {message}")
        else:
            print(f"Received data: {type_data} {tmp_id} {message}")

    def send_promised(self, player: str, channel: str,
                      message: str) -> Promise:
        tmp_id = self.send(player, channel, message, self._get_response)
        self.promised[tmp_id] = Promise()
        return self.promised[tmp_id]

    def send_sync(self, player: str, channel: str,
                  message: str) -> tuple[str, str]:
        promise = self.send_promised(player, channel, message)
        promise.wait(promise)
        return promise.get()

    def stop(self) -> None:
        self.runner.close()
        self.runner.join()
