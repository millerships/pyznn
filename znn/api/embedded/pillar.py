from znn.client.websocket import get_default_client
from znn.constants import PILLAR_REGISTER_ZNN_AMOUNT
from znn.constants import RPC_MAX_PAGE_SIZE
from znn.embedded.definitions import COMMON_ABI
from znn.embedded.definitions import PILLAR_ABI
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import Address
from znn.model.primitives.address import PILLAR_ADDRESS
from znn.model.primitives.token_standard import QSR_ZTS
from znn.model.primitives.token_standard import ZNN_ZTS


class PillarApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def get_deposited_qsr(self, pillar_address: Address):
        return await self.ws_client.send_request(
            "embedded.pillar.getDepositedQsr", [str(pillar_address)]
        )

    async def get_uncollected_reward(self, pillar_address: Address):
        return await self.ws_client.send_request(
            "embedded.pillar.getUncollectedReward", [str(pillar_address)]
        )

    async def get_frontier_reward_by_page(
        self, pillar_address: Address, page_index=0, page_size=RPC_MAX_PAGE_SIZE
    ):
        return await self.ws_client.send_request(
            "embedded.pillar.getFrontierRewardByPage",
            [str(pillar_address), page_index, page_size],
        )

    async def get_qsr_registration_cost(self):
        return await self.ws_client.send_request(
            "embedded.pillar.getQsrRegistrationCost", []
        )

    async def get_all(self, page_index=0, page_size=RPC_MAX_PAGE_SIZE):
        return await self.ws_client.send_request(
            "embedded.pillar.getAll", [page_index, page_size]
        )

    async def get_by_owner(self, pillar_address: Address):
        return await self.ws_client.send_request(
            "embedded.pillar.getByOwner", [str(pillar_address)]
        )

    async def get_by_name(self, pillar_name: str):
        return await self.ws_client.send_request(
            "embedded.pillar.getByName", [pillar_name]
        )

    async def check_name_availability(self, name: str):
        return await self.ws_client.send_request(
            "embedded.pillar.checkNameAvailability", [name]
        )

    async def get_delegated_pillar(self, pillar_address: Address):
        return await self.ws_client.send_request(
            "embedded.pillar.getDelegatedPillar", [str(pillar_address)]
        )

    def register(
        self,
        name: str,
        producer_address: Address,
        reward_address: Address,
        give_block_reward_percentage: int = 0,
        give_delegate_reward_percentage: int = 100,
    ):

        return AccountBlock.contract_call(
            PILLAR_ADDRESS,
            ZNN_ZTS,
            int(PILLAR_REGISTER_ZNN_AMOUNT),
            PILLAR_ABI.encode(
                "Register",
                [
                    name,
                    producer_address,
                    reward_address,
                    give_block_reward_percentage,
                    give_delegate_reward_percentage,
                ],
            ),
        )

    def register_legacy(
        self,
        name: str,
        producer_address: Address,
        reward_address: Address,
        public_key: str,
        signature: str,
        give_block_reward_percentage: int = 0,
        give_delegate_reward_percentage: int = 100,
    ):

        return AccountBlock.contract_call(
            PILLAR_ADDRESS,
            ZNN_ZTS,
            int(PILLAR_REGISTER_ZNN_AMOUNT),
            PILLAR_ABI.encode(
                "RegisterLegacy",
                [
                    name,
                    producer_address,
                    reward_address,
                    give_block_reward_percentage,
                    give_delegate_reward_percentage,
                    public_key,
                    signature,
                ],
            ),
        )

    def update_pillar(
        self,
        name: str,
        producer_address: Address,
        reward_address: Address,
        give_block_reward_percentage: int = 0,
        give_delegate_reward_percentage: int = 100,
    ):

        return AccountBlock.contract_call(
            PILLAR_ADDRESS,
            ZNN_ZTS,
            0,
            PILLAR_ABI.encode(
                "UpdatePillar",
                [
                    name,
                    producer_address,
                    reward_address,
                    give_block_reward_percentage,
                    give_delegate_reward_percentage,
                ],
            ),
        )

    def revoke(
        self, name: str,
    ):
        return AccountBlock.contract_call(
            PILLAR_ADDRESS, ZNN_ZTS, 0, PILLAR_ABI.encode("Revoke", [name],),
        )

    def delegate(
        self, name: str,
    ):
        return AccountBlock.contract_call(
            PILLAR_ADDRESS, ZNN_ZTS, 0, PILLAR_ABI.encode("Delegate", [name],),
        )

    def undelegate(self,):
        return AccountBlock.contract_call(
            PILLAR_ADDRESS, ZNN_ZTS, 0, PILLAR_ABI.encode("Undelegate", [],),
        )

    def collect_reward(self,):
        return AccountBlock.contract_call(
            PILLAR_ADDRESS, ZNN_ZTS, 0, COMMON_ABI.encode("CollectReward", [],),
        )

    def deposit_qsr(self, amount: int):
        return AccountBlock.contract_call(
            PILLAR_ADDRESS, QSR_ZTS, amount, COMMON_ABI.encode("DepositQsr", [],),
        )

    def withdraw_qsr(self,):
        return AccountBlock.contract_call(
            PILLAR_ADDRESS, ZNN_ZTS, 0, COMMON_ABI.encode("WithdrawQsr", [],),
        )
