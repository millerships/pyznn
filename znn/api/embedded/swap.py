from znn.client.websocket import get_default_client
from znn.embedded.definitions import SWAP_ABI
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import SWAP_ADDRESS
from znn.model.primitives.token_standard import ZNN_ZTS


class SwapApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def get_assets(self):
        return await self.ws_client.send_request("embedded.swap.getAssets", [])

    async def get_assets_by_key_id_hash(self, key_id_hash: str):
        return await self.ws_client.send_request(
            "embedded.swap.getAssetsByKeyIdHash", [key_id_hash],
        )

    async def get_legacy_pillars(self):
        return await self.ws_client.send_request("embedded.swap.getLegacyPillars", [])

    def retrieve_assets(self, public_key: str, signature: str):
        return AccountBlock.contract_call(
            SWAP_ADDRESS,
            ZNN_ZTS,
            0,
            SWAP_ABI.encode("RetrieveAssets", [public_key, signature]),
        )
