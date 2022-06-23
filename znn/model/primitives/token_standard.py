import bech32

HRP = "zts"


class TokenStandard:
    def __init__(self, hrp: str, core: bytes):
        self.hrp = hrp
        self.core = core

    def __str__(self):
        return bech32.bech32_encode(self.hrp, bech32.convertbits(self.core, 8, 5, True))

    @staticmethod
    def parse(token_standard: str):
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
        hrp, bcore = bech32.bech32_decode(token_standard)
        core = bech32.convertbits(bcore, 5, 8, False)
        return TokenStandard(hrp, core)

    @staticmethod
    def from_hex(ts_hex: str):
        return TokenStandard(HRP, bytes.fromhex(ts_hex))

    @property
    def core_to_hex(self):
        return f"0x{bytes(self.core).hex()}"


EMPTY_ZTS = TokenStandard.parse("zts1qqqqqqqqqqqqqqqqtq587y")
ZNN_ZTS = TokenStandard.parse("zts1znnxxxxxxxxxxxxx9z4ulx")
QSR_ZTS = TokenStandard.parse("zts1qsrxxxxxxxxxxxxxmrhjll")
