from znn.model.primitives.token_standard import TokenStandard


class TestTokenStandard:
    address = "zts1znnxxxxxxxxxxxxx9z4ulx"

    def test_parse(self):
        t = TokenStandard.parse(self.address)
        assert str(t) == self.address
        assert t.hrp == "zts"
