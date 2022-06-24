from znn.client.websocket import get_default_client
from znn.constants import RPC_MAX_PAGE_SIZE
from znn.embedded.definitions import PLASMA_ABI
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import Address
from znn.model.primitives.address import PLASMA_ADDRESS
from znn.model.primitives.hash import Hash
from znn.model.primitives.token_standard import QSR_ZTS
from znn.model.primitives.token_standard import ZNN_ZTS


class PlasmaApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    def get_plasma_by_qsr(self, qsr_amount):
        return int(qsr_amount) * 2100

    async def get(self, address: Address):
        return await self.ws_client.send_request("embedded.plasma.get", [str(address)])

    async def get_entries_by_address(
        self, address: Address, page_index=0, page_size=RPC_MAX_PAGE_SIZE
    ):
        return await self.ws_client.send_request(
            "embedded.plasma.getEntriesByAddress",
            [str(address), page_index, page_size],
        )

    async def get_required_fusion_amount(self, required_plasma: int):
        return await self.ws_client.send_request(
            "embedded.plasma.getRequiredFusionAmount", [required_plasma]
        )

    async def get_required_pow_for_account_block(self, pow_param):
        # pow_param is json data
        return await self.ws_client.send_request(
            "embedded.plasma.getRequiredPoWForAccountBlock", [pow_param]
        )

    def fuse(
        self, beneficiary: Address, amount: int,
    ):

        return AccountBlock.contract_call(
            PLASMA_ADDRESS, QSR_ZTS, amount, PLASMA_ABI.encode("Fuse", [beneficiary],),
        )

    def cancel(
        self, hash_id: Hash,
    ):

        return AccountBlock.contract_call(
            PLASMA_ADDRESS, ZNN_ZTS, 0, PLASMA_ABI.encode("CancelFuse", [hash_id],),
        )
