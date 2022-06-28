from znn.api.embedded.plasma import PlasmaApi
from znn.api.ledger import LedgerApi
from znn.model.nom.account_block import AccountBlock
from znn.model.primitives.address import Address
from znn.model.primitives.hash import Hash
from znn.model.primitives.hash_height import HashHeight
from znn.model.primitives.token_standard import TokenStandard
from znn.wallet.keypair import KeyPair


class Transact:
    def __init__(self, private_key: str):
        self.keypair = KeyPair(private_key)

    async def fast_forward_block(self, account_block: AccountBlock):
        account_block.address = self.keypair.address
        account_block.public_key = bytes.fromhex(self.keypair.public_key)

        ledger_api = LedgerApi()
        frontier = await ledger_api.get_frontier_account_block(
            str(self.keypair.address)
        )

        if frontier is None:
            account_block.height = 1
        else:
            account_block.height = frontier["height"] + 1
            account_block.previous_hash = Hash.parse(frontier["hash"])

        momentum = await ledger_api.get_frontier_momentum()
        account_block.momentum_acknowledged = HashHeight(
            momentum["height"], Hash.parse(momentum["hash"])
        )

        plasma_api = PlasmaApi()
        req_pow = await plasma_api.get_internal_required_pow_for_account_block(
            account_block
        )

        if req_pow["requiredDifficulty"] != 0:
            raise Exception(
                f"Unable to produce plasma using PoW. Fuse to {str(self.keypair.address)}"
            )

        account_block.fused_plasma = req_pow["basePlasma"]

        account_block.hash = account_block.get_hash()
        account_block.signature = self.keypair.sign(account_block.hash)
        return await ledger_api.publish_raw_transaction(account_block)

    async def send(self, to_address: Address, zts: TokenStandard, amount: int):
        kwargs = {
            "to_address": to_address,
            "token_standard": zts,
            "amount": amount,
            "block_type": 2,  # user send
        }
        account_block = AccountBlock(**kwargs)
        return await self.fast_forward_block(account_block)

    async def receive(self, from_block_hash: Hash):
        kwargs = {"from_block_hash": from_block_hash, "block_type": 3}  # user receive
        account_block = AccountBlock(**kwargs)
        return self.fast_forward_block(account_block)
