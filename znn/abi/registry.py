from eth_abi.registry import registry
from eth_abi.utils.padding import zpad

from znn.model.primitives.address import Address
from znn.model.primitives.hash import Hash
from znn.model.primitives.token_standard import TokenStandard

DATA_BYTE_SIZE = 32
ZTS_BYTE_SIZE = 20
ADDRESS_BYTES_SIZE = 40


def encode_hash(value):
    if isinstance(value, Hash):
        return bytes.fromhex(str(value))

    if type(value) == str:
        if value[:2] == "0x":
            return bytes.fromhex(value[2:])
        return bytes.fromhex(value)

    return value


def decode_hash(stream):
    value = stream.read(DATA_BYTE_SIZE)
    return f"0x{value.hex()}"


def encode_token_standard(value):
    if isinstance(value, TokenStandard):
        result = value.core_to_hex

    if type(value) == str:
        result = TokenStandard.parse(value).core_to_hex

    result = bytes.fromhex(result[2:])
    padded_encoded_value = zpad(result, DATA_BYTE_SIZE)
    return padded_encoded_value


def decode_token_standard(stream):
    value = stream.read(DATA_BYTE_SIZE)
    return value.hex()[-ZTS_BYTE_SIZE:]


def encode_address(value):
    result = value
    if isinstance(value, Address):
        result = value.core_to_hex

    if type(value) == str:
        result = Address.parse(value).core_to_hex

    result = bytes.fromhex(result[2:])
    padded_encoded_value = zpad(result, DATA_BYTE_SIZE)
    return padded_encoded_value


def decode_address(stream):
    value = stream.read(DATA_BYTE_SIZE)
    return value.hex()[-ADDRESS_BYTES_SIZE:]


registry.register("hash", encode_hash, decode_hash)
registry.unregister("address")
registry.register("address", encode_address, decode_address)
registry.register("tokenStandard", encode_token_standard, decode_token_standard)
