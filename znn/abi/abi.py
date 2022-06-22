import json
from typing import List

from eth_abi import decode_abi
from eth_abi import encode_abi

from znn.abi.utils import get_function_signature
from znn.model.primitives.address import Address
from znn.model.primitives.hash import Hash
from znn.model.primitives.token_standard import TokenStandard


class ABI:
    def __init__(self, data: List):
        self.entries = []
        self.fn_name_map = {}
        for entry in data:
            if entry["type"] == "function":
                self.entries.append(
                    {"name": entry["name"], "inputs": entry["inputs"],}
                )
                self.fn_name_map[entry["name"]] = entry["inputs"]

    @staticmethod
    def from_json(json_data):
        # The example format of json_data can be found in embedded/definitions.py
        data = json.loads(json_data)
        return ABI(data)

    def _parse_type(self, param_type, value):
        if param_type == "address":
            return str(Address.from_hex(value))
        if param_type == "tokenStandard":
            return str(TokenStandard.from_hex(value))
        return f"0x{value}"

    def encode(self, fn_name: str, fn_params: List):
        if fn_name not in self.fn_name_map:
            raise Exception("Function not found in the ABI registry")

        fn_inputs = self.fn_name_map[fn_name]
        if len(fn_inputs) != len(fn_params):
            raise Exception(
                f"Unexpected input params length, expected {len(fn_inputs)}"
            )

        # Encoding func signature
        fn_signature = get_function_signature(fn_name, fn_inputs)
        fn_hash = Hash.digest(fn_signature.encode())
        fn_hash_prefix = fn_hash.core.hex()[:8]

        # Encoding func params
        encoded_params = encode_abi([i["type"] for i in fn_inputs], fn_params).hex()

        return bytes.fromhex(f"{fn_hash_prefix}{encoded_params}")

    def decode(self, fn_name: str, data: bytes):
        if fn_name not in self.fn_name_map:
            raise Exception("Function not found in the ABI registry")

        fn_inputs = self.fn_name_map[fn_name]
        encoded_params = data[4:]
        decoded_tuple = decode_abi([i["type"] for i in fn_inputs], encoded_params)

        response = {}
        for i in range(len(fn_inputs)):
            response[fn_inputs[i]["name"]] = self._parse_type(
                fn_inputs[i]["type"], decoded_tuple[i]
            )
        return response
