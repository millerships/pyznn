from znn.client.websocket import get_default_client
from znn.constants import MEMORY_POOL_PAGE_SIZE
from znn.constants import RPC_MAX_PAGE_SIZE
from znn.model.nom.account_block import AccountBlock


class LedgerApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def publish_raw_transaction(self, account_block: AccountBlock):
        return await self.ws_client.send_request(
            "ledger.publishRawTransaction", [account_block.to_json()]
        )

    async def get_unconfirmed_blocks_by_address(
        self, address: str, page_index=0, page_size=MEMORY_POOL_PAGE_SIZE
    ):
        """Get list of account blocks that have not been included into a momentum yet."""
        return await self.ws_client.send_request(
            "ledger.getUnconfirmedBlocksByAddress", [address, page_index, page_size]
        )

    async def get_unreceived_blocks_by_address(
        self, address: str, page_index=0, page_size=MEMORY_POOL_PAGE_SIZE
    ):
        """Get list of account blocks that don't have a corresponding receive-account-block."""
        return await self.ws_client.send_request(
            "ledger.getUnreceivedBlocksByAddress", [address, page_index, page_size]
        )

    async def get_frontier_account_block(self, address: str):
        """Get last account block of the specified address."""
        return await self.ws_client.send_request(
            "ledger.getFrontierAccountBlock", [address]
        )

    async def get_account_block_by_hash(self, hashstr: str):
        """Get the account block with the specified hash."""
        return await self.ws_client.send_request(
            "ledger.getAccountBlockByHash", [hashstr]
        )

    async def get_account_blocks_by_height(
        self, address: str, height=1, count=RPC_MAX_PAGE_SIZE
    ):
        """Get list of account blocks for the account-chain with the specified address."""
        return await self.ws_client.send_request(
            "ledger.getAccountBlocksByHeight", [address, height, count]
        )

    async def get_account_blocks_by_page(
        self, address: str, page_index=1, page_size=RPC_MAX_PAGE_SIZE
    ):
        """Get list of account blocks for the account-chain of address by page.

        pageIndex = 0 returns the most recent account blocks sorted descending by height
        """
        return await self.ws_client.send_request(
            "ledger.getAccountBlocksByPage", [address, page_index, page_size]
        )

    async def get_frontier_momentum(self):
        """Get the latest momentum."""
        return await self.ws_client.send_request("ledger.getFrontierMomentum", [])

    async def get_momentum_before_time(self, time: int):
        """Get the momentum for the period before the specified time."""
        return await self.ws_client.send_request("ledger.getMomentumBeforeTime", [time])

    async def get_momentum_by_hash(self, hashstr: str):
        """Get the momentum with the specified hash."""
        return await self.ws_client.send_request("ledger.getMomentumByHash", [hashstr])

    async def get_momentums_by_page(self, page_index=1, page_size=RPC_MAX_PAGE_SIZE):
        """Get list of momentums by page."""
        return await self.ws_client.send_request(
            "ledger.getMomentumsByPage", [page_index, page_size]
        )

    async def get_momentums_by_height(self, height=1, count=RPC_MAX_PAGE_SIZE):
        """Get list of momentums from height to height + count."""
        return await self.ws_client.send_request(
            "ledger.getMomentumsByHeight", [height, count]
        )

    async def get_detailed_momentums_by_height(self, height=1, count=RPC_MAX_PAGE_SIZE):
        """Get detailed list of momentums from height to height + count.

        This contains extra information about the account blocks they contain.
        """
        return await self.ws_client.send_request(
            "ledger.getDetailedMomentumsByHeight", [height, count]
        )

    async def get_account_info_by_address(self, address: str):
        """Get information about the account-chain of the specified address."""
        return await self.ws_client.send_request(
            "ledger.getAccountInfoByAddress", [address]
        )
