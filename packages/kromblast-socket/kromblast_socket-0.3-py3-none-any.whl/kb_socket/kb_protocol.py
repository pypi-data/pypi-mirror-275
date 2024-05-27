from typing import Tuple


class KbProtocol:
    def _test(self, data: str, invalid: str) -> bool:
        return list(set(data) & set(invalid))

    def build_message(self, player: str, tmp_id: str, channel: str,
                      message: str) -> bytes:
        if (self._test(player, ['\1\2\0|'])):
            raise ValueError('Invalid player')
        if (self._test(tmp_id, ['\1\2\0'])):
            raise ValueError('Invalid tmp_id')
        if (self._test(channel, ['\1\2\0:'])):
            raise ValueError('Invalid channel')
        if (self._test(message, ['\1\2\0'])):
            raise ValueError('Invalid message')
        return f'\1{player}|{tmp_id}\2{channel}:{message}'.encode()

    def parse_response(self, data: bytes) -> Tuple[str, str, str]:
        data = data.decode()
        if data[0] != '\1':
            raise ValueError('Invalid data')
        type_data, data = data[1:].split('|', 1)
        tmp_id, message = data.split('\2', 1)
        return type_data, tmp_id, message
