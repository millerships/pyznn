from znn.client.websocket import get_default_client
from znn.constants import RPC_MAX_PAGE_SIZE
from znn.constants import SENTINEL_REGISTER_ZNN_AMOUNT
from znn.embedded.definitions import COMMON_ABI
from znn.embedded.definitions import SENTINEL_ABI
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import Address
from znn.model.primitives.address import SENTINEL_ADDRESS
from znn.model.primitives.token_standard import QSR_ZTS
from znn.model.primitives.token_standard import ZNN_ZTS


class SentinelApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def get_all_active(self, page_index=0, page_size=RPC_MAX_PAGE_SIZE):
        return await self.ws_client.send_request(
            "embedded.sentinel.getAllActive", [page_index, page_size],
        )

    async def get_by_owner(self, address: Address):
        return await self.ws_client.send_request(
            "embedded.sentinel.getByOwner", [str(address)]
        )

    async def get_deposited_qsr(self, address: Address):
        return await self.ws_client.send_request(
            "embedded.sentinel.getDepositedQsr", [str(address)]
        )

    async def get_uncollected_reward(self, pillar_address: Address):
        return await self.ws_client.send_request(
            "embedded.sentinel.getUncollectedReward", [str(pillar_address)]
        )

    async def get_frontier_reward_by_page(
        self, address: Address, page_index=0, page_size=RPC_MAX_PAGE_SIZE
    ):
        return await self.ws_client.send_request(
            "embedded.sentinel.getFrontierRewardByPage",
            [str(address), page_index, page_size],
        )

    def register(self,):

        return AccountBlock.contract_call(
            SENTINEL_ADDRESS,
            ZNN_ZTS,
            int(SENTINEL_REGISTER_ZNN_AMOUNT),
            SENTINEL_ABI.encode("Register", [],),
        )

    def revoke(self,):
        return AccountBlock.contract_call(
            SENTINEL_ABI, ZNN_ZTS, 0, SENTINEL_ABI.encode("Revoke", [],),
        )

    def collect_reward(self,):
        return AccountBlock.contract_call(
            SENTINEL_ADDRESS, ZNN_ZTS, 0, COMMON_ABI.encode("CollectReward", [],),
        )

    def deposit_qsr(self, amount: int):
        return AccountBlock.contract_call(
            SENTINEL_ADDRESS, QSR_ZTS, amount, COMMON_ABI.encode("DepositQsr", [],),
        )

    def withdraw_qsr(self,):
        return AccountBlock.contract_call(
            SENTINEL_ADDRESS, ZNN_ZTS, 0, COMMON_ABI.encode("WithdrawQsr", [],),
        )
