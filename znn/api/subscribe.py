from znn.client.websocket import get_default_client


class SubscribeApi:
    """Subscribe to messages.

    Example:
    -------
    In [1]: from znn.api.subscribe import *

    In [2]: s = SubscribeApi()

    In [3]: await s.to_all_account_blocks()
    {"jsonrpc":"2.0","id":1,"result":"0x9665f891f28a9bddcff1d538d4a793f6"}

    {"jsonrpc":"2.0","method":"ledger.subscription","params":{"subscription":"0x9665f891f28a9bddcff1d538d4a793f6","result":[{"blockType":3,"hash":"f71d9646238ee4d6ee11a79688f6100c5c5e05adc7373a38928d69a0de662269","height":55,"address":"z1qpq6wzg65y5grxzjlru86ewctd073unt0tdr6c","toAddress":"z1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsggv2f","fromHash":"b95a070591dbb679ad973768218d65198f21af2647791b6a9f782cae74a59ddd"},{"blockType":3,"hash":"5777fbb8f4b370879b0be84cfa6bac91a5d40ab524ee738ab14d79dd908d7ca6","height":54,"address":"z1qpepk82nwjtz7wruv45r0xteaw3fapwg4786t8","toAddress":"z1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsggv2f","fromHash":"90ef9bf3cd9f140b0cfef3763936cbd742b18b1110a940e53dba5ecd6e8fe531"},{"blockType":3,"hash":"216c5eb2c6a035d65f115d357291a2cca94151d7d5408848a8cb8d4a8beb62b2","height":54,"address":"z1qrv4sjc8t9w06370zq3qlywl3xhen9z30y73dl","toAddress":"z1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsggv2f","fromHash":"91862f9e1ca1195cc1fecea8138cd998166a026987101d59f1be3b1279b2207a"}]}}

    {"jsonrpc":"2.0","method":"ledger.subscription","params":{"subscription":"0x9665f891f28a9bddcff1d538d4a793f6","result":[{"blockType":2,"hash":"119c024fac7d08c583da9426b3fcfdce3ffa76e6ded90200ea62219b8e6a0a6b","height":977,"address":"z1qplewmqccyjahd5pvfc6ce3d2yy4340erm6u4e","toAddress":"z1qqpuw9c8cvg5kpe7ev03mre2ee04rner7xgjqd","fromHash":"0000000000000000000000000000000000000000000000000000000000000000"}]}}
    .
    .
    .
    This will run forever.
    """

    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def to_momentums(self):
        return await self.ws_client.send_and_listen("ledger.subscribe", ["momentums"])

    async def to_all_account_blocks(self):
        return await self.ws_client.send_and_listen(
            "ledger.subscribe", ["allAccountBlocks"]
        )

    async def to_account_blocks_by_address(self, address: str):
        return await self.ws_client.send_and_listen(
            "ledger.subscribe", ["accountBlocksByAddress", address]
        )

    async def to_unreceived_account_blocks_by_address(self, address: str):
        return await self.ws_client.send_and_listen(
            "ledger.subscribe", ["unreceivedAccountBlocksByAddress", address]
        )
