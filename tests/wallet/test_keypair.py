import ed25519
import pytest

from znn.wallet.keypair import KeyPair
from znn.wallet.keypair import verify_signature


class TestKeyPair:
    private_key_hex = "d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863"

    def test_sign_and_verify(self):
        keypair = KeyPair(self.private_key_hex)
        signed_msg = keypair.sign("Hello, aliens")
        verify_signature(keypair.public_key, signed_msg.decode(), "Hello, aliens")

    def test_sign_and_verify_raises_exception(self):
        keypair = KeyPair(self.private_key_hex)
        signed_msg = keypair.sign("Hello, aliens")
        with pytest.raises(ed25519.BadSignatureError) as excinfo:
            verify_signature(keypair.public_key, signed_msg.decode(), "Hello, humans")
        assert "Bad Signature" in str(excinfo.value)
