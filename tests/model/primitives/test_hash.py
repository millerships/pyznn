from znn.model.primitives.hash import Hash


class TestHash:
    data_bytes = b"hello world"
    message_hex = "644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938"

    def test_digest(self):
        h = Hash.digest(self.data_bytes)
        assert str(h) == self.message_hex

    def test_parse(self):
        h = Hash.parse(self.message_hex)
        assert str(h) == self.message_hex
