from znn.model.primitives.address import Address


class TestAddress:
    core = [
        0,
        37,
        55,
        74,
        65,
        159,
        50,
        115,
        111,
        97,
        236,
        197,
        172,
        64,
        89,
        210,
        241,
        181,
        136,
        77,
    ]
    address = "z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7"
    public_key_hex = "3e13d7238d0e768a567dce84b54915f2323f2dcd0ef9a716d9c61abed631ba10"

    def test_from_public_key_hex(self):
        a = Address.from_public_key_hex(self.public_key_hex)
        assert str(a) == self.address
        assert a.hrp == "z"
        assert a.core == self.core

    def test_parse(self):
        a = Address.parse(self.address)
        assert str(a) == self.address
        assert a.hrp == "z"
        assert a.core == self.core
