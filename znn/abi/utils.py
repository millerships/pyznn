import itertools
import re
from typing import List

from eth_utils import to_tuple


DYNAMIC_TYPES = ["bytes", "string"]

INT_SIZES = range(8, 257, 8)
BYTES_SIZES = range(1, 33)
UINT_TYPES = [f"uint{i}" for i in INT_SIZES]
INT_TYPES = [f"int{i}" for i in INT_SIZES]
BYTES_TYPES = [f"bytes{i}" for i in BYTES_SIZES] + ["bytes32.byte"]

STATIC_TYPES = list(
    itertools.chain(["address", "bool"], UINT_TYPES, INT_TYPES, BYTES_TYPES,)
)

BASE_TYPE_REGEX = "|".join(
    (_type + "(?![a-z0-9])" for _type in itertools.chain(STATIC_TYPES, DYNAMIC_TYPES))
)

SUB_TYPE_REGEX = r"\[" "[0-9]*" r"\]"

TYPE_REGEX = ("^" "(?:{base_type})" "(?:(?:{sub_type})*)?" "$").format(
    base_type=BASE_TYPE_REGEX, sub_type=SUB_TYPE_REGEX,
)


def is_recognized_type(abi_type) -> bool:
    return bool(re.match(TYPE_REGEX, abi_type))


NAME_REGEX = "[a-zA-Z_]" "[a-zA-Z0-9_]*"


ENUM_REGEX = ("^" "{lib_name}" r"\." "{enum_name}" "$").format(
    lib_name=NAME_REGEX, enum_name=NAME_REGEX
)


def is_probably_enum(abi_type) -> bool:
    return bool(re.match(ENUM_REGEX, abi_type))


@to_tuple
def normalize_event_input_types(abi_args):
    for arg in abi_args:
        if is_recognized_type(arg["type"]):
            yield arg
        elif is_probably_enum(arg["type"]):
            yield {k: "uint8" if k == "type" else v for k, v in arg.items()}
        else:
            yield arg


def get_function_signature(fn_name: str, inputs: List) -> str:
    function_signature = "{fn_name}({fn_input_types})".format(
        fn_name=fn_name,
        fn_input_types=",".join(
            [arg["type"] for arg in normalize_event_input_types(inputs)]
        ),
    )
    return function_signature
