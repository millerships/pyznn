import logging

import websockets
from jsonrpcclient import Ok
from jsonrpcclient import parse_json
from jsonrpcclient import request_json


class WsClient:
    def __init__(self, url: str):
        self.url = url

    async def send_request(self, method: str, params):
        async with websockets.connect(self.url) as ws:
            await ws.send(request_json(method, params))
            response = parse_json(await ws.recv())
            if isinstance(response, Ok):
                return response.result
            else:
                logging.error(response.message)


def get_default_client():
    """Get ws client for quick testing/playing."""
    return WsClient("ws://nodes.zenon.place:35998")
