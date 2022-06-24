from znn.client.websocket import get_default_client
from znn.constants import RPC_MAX_PAGE_SIZE
from znn.constants import TOKEN_ISSUE_ZNN_FEE
from znn.embedded.definitions import TOKEN_ABI
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import Address
from znn.model.primitives.address import TOKEN_ADDRESS
from znn.model.primitives.token_standard import TokenStandard
from znn.model.primitives.token_standard import ZNN_ZTS


class TokenApi:
    def __init__(self, ws_client=None):
        self.ws_client = ws_client

        if self.ws_client is None:
            self.ws_client = get_default_client()

    async def get_all(self, page_index=0, page_size=RPC_MAX_PAGE_SIZE):
        return await self.ws_client.send_request(
            "embedded.token.getAll", [page_index, page_size],
        )

    async def get_by_owner_address(
        self, address: Address, page_index=0, page_size=RPC_MAX_PAGE_SIZE
    ):
        return await self.ws_client.send_request(
            "embedded.token.getByOwner", [str(address), page_index, page_size],
        )

    async def get_by_zts(self, token_standard: TokenStandard):
        return await self.ws_client.send_request(
            "embedded.token.getByZts", [str(token_standard)],
        )

    def issue_token(
        self,
        token_name: str,
        token_symbol: str,
        token_domain: str,
        total_supply: int,
        max_supply: int,
        decimals: int,
        mintable: bool,
        burnable: bool,
        utility: bool,
    ):
        return AccountBlock.contract_call(
            TOKEN_ADDRESS,
            ZNN_ZTS,
            TOKEN_ISSUE_ZNN_FEE,
            TOKEN_ABI.encode(
                "IssueToken",
                [
                    token_name,
                    token_symbol,
                    token_domain,
                    total_supply,
                    max_supply,
                    decimals,
                    mintable,
                    burnable,
                    utility,
                ],
            ),
        )

    def mint_token(
        self, token_standard: TokenStandard, amount: int, receive_address: Address
    ):
        return AccountBlock.contract_call(
            TOKEN_ADDRESS,
            ZNN_ZTS,
            0,
            TOKEN_ABI.encode("Mint", [token_standard, amount, receive_address,]),
        )

    def burn_token(self, token_standard: TokenStandard, amount: int):
        return AccountBlock.contract_call(
            TOKEN_ADDRESS, token_standard, amount, TOKEN_ABI.encode("Burn", []),
        )

    def update_token(
        self,
        token_standard: TokenStandard,
        owner_address: Address,
        is_mintable: bool,
        is_burnable: bool,
    ):
        return AccountBlock.contract_call(
            TOKEN_ADDRESS,
            ZNN_ZTS,
            0,
            TOKEN_ABI.encode(
                "UpdateToken", [token_standard, owner_address, is_mintable, is_burnable]
            ),
        )
