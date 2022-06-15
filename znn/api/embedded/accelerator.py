from znn.client.websocket import get_default_client
from znn.constants import ONE_ZNN
from znn.constants import RPC_MAX_PAGE_SIZE
from znn.embedded.constants import PROJECT_CREATION_FEE_ZNN
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import ACCELERATOR_ADDRESS
from znn.model.primitives.token_standard import ZNN_ZTS


class AcceleratorApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def get_account_blocks_by_page(
        self, page_index=0, page_size=RPC_MAX_PAGE_SIZE
    ):
        return await self.ws_client.send_request(
            "embedded.accelerator.getAll", [page_index, page_size]
        )

    async def get_project_by_id(self, project_id: str):
        return await self.ws_client.send_request(
            "embedded.accelerator.getProjectById", [project_id]
        )

    async def get_phase_by_id(self, phase_id: str):
        return await self.ws_client.send_request(
            "embedded.accelerator.getPhaseById", [phase_id]
        )

    async def get_pillar_votes(self, name: str, hashes):
        return await self.ws_client.send_request(
            "embedded.accelerator.getPillarVotes", [name, hashes]
        )

    async def get_vote_breakdown(self, hash_id: str):
        return await self.ws_client.send_request(
            "embedded.accelerator.getVoteBreakdown", [hash_id]
        )

    async def create_project(
        self,
        name: str,
        description: str,
        url: str,
        znn_funds_needed: int,
        qsr_funds_needed: int,
    ):

        return AccountBlock.contract_call(
            ACCELERATOR_ADDRESS, ZNN_ZTS, int(PROJECT_CREATION_FEE_ZNN * ONE_ZNN), None
        )
