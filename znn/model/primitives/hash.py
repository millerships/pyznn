import hashlib


class Hash:
    def __init__(self, core: bytes):
        self.core = core

    def __str__(self):
        return self.core.hex()

    @staticmethod
    def parse(hex_str: str):
        return Hash(bytes.fromhex(hex_str))

    @staticmethod
    def digest(data_bytes: bytes):
        core = hashlib.sha3_256(data_bytes).digest()
        return Hash(core)


EMPTY_HASH = Hash.parse(
    "0000000000000000000000000000000000000000000000000000000000000000"
)
