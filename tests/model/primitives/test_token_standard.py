from znn.model.primitives.token_standard import TokenStandard


class TestTokenStandard:
    address = "zts1znnxxxxxxxxxxxxx9z4ulx"
    core_hex = "0x14e66318c6318c6318c6"

    def test_parse(self):
        t = TokenStandard.parse(self.address)
        assert str(t) == self.address
        assert t.hrp == "zts"
        assert t.core_to_hex == self.core_hex
