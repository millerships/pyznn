from znn.model.primitives.address import EMPTY_ADDRESS
from znn.model.primitives.hash import EMPTY_HASH
from znn.model.primitives.hash_height import EMPTY_HASH_HEIGHT
from znn.model.primitives.token_standard import EMPTY_ZTS


class AccountBlock:
    def __init__(self):
        self.version = 1
        self.block_type = 0
        self.chain_identifier = 1
        self.from_block_hash = EMPTY_HASH
        self.hash = EMPTY_HASH
        self.previous_hash = EMPTY_HASH
        self.height = 0
        self.momentum_acknowledged = EMPTY_HASH_HEIGHT
        self.address = EMPTY_ADDRESS
        self.to_address = EMPTY_ADDRESS
        self.amount = 0
        self.token_standard = EMPTY_ZTS
        self.fused_plasma = 0
        self.data = bytes.fromhex("")
        self.difficulty = 0
        self.nonce = bytes.fromhex("0000000000000000")
        self.public_key = None
        self.signature = None
