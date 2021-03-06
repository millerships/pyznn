import hashlib

import bech32

HRP = "z"


class Address:
    def __init__(self, hrp: str, core: bytes):
        self.hrp = hrp
        self.core = core

    def __str__(self):
        return bech32.bech32_encode(self.hrp, bech32.convertbits(self.core, 8, 5, True))

    @staticmethod
    def from_public_key_hex(public_key_hex: str):
        """Get Address instance from public key hex string.

        Parameters
        ----------
        public_key_hex : str
            Without the leading 0x

        Example
        -------
        In [0]: pubkey_hex = "3e13d7238d0e768a567dce84b54915f2323f2dcd0ef9a716d9c61abed631ba10"
        In [0]: a = Address.from_public_key_hex(pubkey_hex)

        In [1]: str(a) # Also, check a.__dict__
        Out[1]: 'z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7'
        """
        core = [0] + list(hashlib.sha3_256(bytes.fromhex(public_key_hex)).digest())[:19]
        return Address(HRP, core)

    @staticmethod
    def parse(address: str):
        """Get Address instance from bech32 encoded address string.

        Parameters
        ----------
        address : str
            For example, z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7

        Returns
        -------
        Address instance

        Example
        -------
        In [0]: a = Address.parse("z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7")

        In [1]: str(a) # Also, check a.__dict__
        Out[1]: 'z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7'
        """
        hrp, bcore = bech32.bech32_decode(address)
        core = bech32.convertbits(bcore, 5, 8, False)
        return Address(hrp, core)

    @staticmethod
    def from_hex(address_hex: str):
        return Address(HRP, bytes.fromhex(address_hex))

    @property
    def core_to_hex(self):
        return f"0x{bytes(self.core).hex()}"


EMPTY_ADDRESS = Address.parse("z1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsggv2f")
PLASMA_ADDRESS = Address.parse("z1qxemdeddedxplasmaxxxxxxxxxxxxxxxxsctrp")
PILLAR_ADDRESS = Address.parse("z1qxemdeddedxpyllarxxxxxxxxxxxxxxxsy3fmg")
TOKEN_ADDRESS = Address.parse("z1qxemdeddedxt0kenxxxxxxxxxxxxxxxxh9amk0")
SENTINEL_ADDRESS = Address.parse("z1qxemdeddedxsentynelxxxxxxxxxxxxxwy0r2r")
STAKE_ADDRESS = Address.parse("z1qxemdeddedxstakexxxxxxxxxxxxxxxxjv8v62")
SWAP_ADDRESS = Address.parse("z1qxemdeddedxswapxxxxxxxxxxxxxxxxxxl4yww")
SPORK_ADDRESS = Address.parse("z1qxemdeddedxsp0rkxxxxxxxxxxxxxxxx956u48")
ACCELERATOR_ADDRESS = Address.parse("z1qxemdeddedxaccelerat0rxxxxxxxxxxp4tk22")
BRIDGE_ADDRESS = Address.parse("z1qzlytaqdahg5t02nz5096frflfv7dm3y7yxmg7")
