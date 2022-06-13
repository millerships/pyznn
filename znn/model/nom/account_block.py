import base64

from znn.model.primitives.address import Address
from znn.model.primitives.address import EMPTY_ADDRESS
from znn.model.primitives.hash import EMPTY_HASH
from znn.model.primitives.hash import Hash
from znn.model.primitives.hash_height import EMPTY_HASH_HEIGHT
from znn.model.primitives.hash_height import HashHeight
from znn.model.primitives.token_standard import EMPTY_ZTS
from znn.model.primitives.token_standard import TokenStandard


class AccountBlock:
    def __init__(self, *args, **kwargs):
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
        self.__dict__.update(kwargs)

    @staticmethod
    def from_json(json_data):
        kwargs = {
            "version": json_data["version"],
            "block_type": json_data["blockType"],
            "chain_identifier": json_data["chainIdentifier"],
            "from_block_hash": Hash.parse(json_data["fromBlockHash"]),
            "hash": Hash.parse(json_data["hash"]),
            "previous_hash": Hash.parse(json_data["previousHash"]),
            "height": json_data["height"],
            "momentum_acknowledged": HashHeight.from_json(
                json_data["momentumAcknowledged"]
            ),
            "address": Address.parse(json_data["address"]),
            "to_address": Address.parse(json_data["toAddress"]),
            "amount": json_data["amount"],
            "token_standard": TokenStandard.parse(json_data["tokenStandard"]),
            "fused_plasma": json_data["fusedPlasma"],
            "data": base64.b64decode(json_data["data"]),
            "difficulty": json_data["difficulty"],
            "nonce": bytes.fromhex(json_data["nonce"]),
            "public_key": base64.b64decode(json_data["publicKey"]),
            "signature": base64.b64decode(json_data["signature"]),
        }
        return AccountBlock(**kwargs)

    def to_json(self):
        return {
            "version": self.version,
            "blockType": self.block_type,
            "chainIdentifier": self.chain_identifier,
            "fromBlockHash": str(self.from_block_hash),
            "hash": str(self.hash),
            "previousHash": str(self.previous_hash),
            "height": self.height,
            "momentumAcknowledged": self.momentum_acknowledged.to_json(),
            "address": str(self.address),
            "toAddress": str(self.to_address),
            "amount": self.amount,
            "tokenStandard": str(self.token_standard),
            "fusedPlasma": self.fused_plasma,
            "data": base64.b64encode(self.data).decode(),
            "difficulty": self.difficulty,
            "nonce": self.nonce.hex(),
            "publicKey": base64.b64encode(self.public_key).decode(),
            "signature": base64.b64encode(self.signature).decode(),
        }

    def get_hash(self):
        return Hash.digest(
            b"".join(
                [
                    self.version.to_bytes(8, "big"),
                    self.chain_identifier.to_bytes(8, "big"),
                    self.block_type.to_bytes(8, "big"),
                    self.previous_hash.core,
                    self.height.to_bytes(8, "big"),
                    self.momentum_acknowledged.hash.core,
                    self.momentum_acknowledged.height.to_bytes(8, "big"),
                    bytes(self.address.core),
                    bytes(self.to_address.core),
                    self.amount.to_bytes(32, "big"),
                    bytes(self.token_standard.core),
                    self.from_block_hash.core,
                    Hash.digest(b"").core,
                    Hash.digest(self.data).core,
                    self.fused_plasma.to_bytes(8, "big"),
                    self.difficulty.to_bytes(8, "big"),
                    self.nonce,
                ]
            )
        )
