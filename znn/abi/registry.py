from eth_abi.registry import registry

from znn.model.primitives.hash import Hash


def encode_hash(value):
    if isinstance(value, Hash):
        return bytes.fromhex(str(value))

    if type(value) == str:
        if value[:2] == "0x":
            return bytes.fromhex(value[2:])
        return bytes.fromhex(value)

    return value


def decode_hash(stream):
    value = stream.read()
    return value.hex()


registry.register("hash", encode_hash, decode_hash)
