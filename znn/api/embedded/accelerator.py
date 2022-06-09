from znn.client.websocket import get_default_client
from znn.constants import RPC_MAX_PAGE_SIZE


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
