from .websocket import WsClient


def get_default_client():
    return WsClient("ws://nodes.zenon.place:35998")
