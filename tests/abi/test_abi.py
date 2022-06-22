from znn.embedded.definitions import STAKE_ABI


class TestABI:
    def test_encode_and_decode(self):
        value = "0x1234567812345678123456781234567812345678123456781234567812345678"
        encoded_bytes = STAKE_ABI.encode("Cancel", [value])
        expected_encoded_hex = "5a92fe321234567812345678123456781234567812345678123456781234567812345678"  # noqa
        assert expected_encoded_hex == encoded_bytes.hex()

        expected_decoded = {"id": value}
        decoded = STAKE_ABI.decode("Cancel", encoded_bytes)
        assert decoded == expected_decoded
