from znn.client.websocket import get_default_client
from znn.constants import RPC_MAX_PAGE_SIZE
from znn.embedded.definitions import COMMON_ABI
from znn.embedded.definitions import STAKE_ABI
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import Address
from znn.model.primitives.address import STAKE_ADDRESS
from znn.model.primitives.hash import Hash
from znn.model.primitives.token_standard import ZNN_ZTS


class StakeApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def get_entries_by_address(
        self, address: Address, page_index=0, page_size=RPC_MAX_PAGE_SIZE
    ):
        return await self.ws_client.send_request(
            "embedded.stake.getEntriesByAddress", [str(address), page_index, page_size],
        )

    async def get_uncollected_reward(self, address: Address):
        return await self.ws_client.send_request(
            "embedded.stake.getUncollectedReward", [str(address)]
        )

    async def get_frontier_reward_by_page(
        self, address: Address, page_index=0, page_size=RPC_MAX_PAGE_SIZE
    ):
        return await self.ws_client.send_request(
            "embedded.stake.getFrontierRewardByPage",
            [str(address), page_index, page_size],
        )

    def stake(
        self, duration_in_sec: int, amount: int,
    ):
        return AccountBlock.contract_call(
            STAKE_ADDRESS,
            ZNN_ZTS,
            amount,
            STAKE_ABI.encode("Stake", [str(duration_in_sec)],),
        )

    def cancel(
        self, hash_id: Hash,
    ):
        return AccountBlock.contract_call(
            STAKE_ADDRESS, ZNN_ZTS, 0, STAKE_ABI.encode("Cancel", [hash_id],),
        )

    def collect_reward(self,):
        return AccountBlock.contract_call(
            STAKE_ADDRESS, ZNN_ZTS, 0, COMMON_ABI.encode("CollectReward", [],),
        )
