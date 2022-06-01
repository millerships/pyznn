import ed25519

from znn.model.primitives.address import Address


class KeyPair:
    def __init__(self, private_key: str):
        # It's easier to work with hex representations of keys
        self.private_key = private_key
        self.signing_key = ed25519.SigningKey(private_key.encode(), encoding="hex")
        self.public_key = (
            self.signing_key.get_verifying_key().to_ascii(encoding="hex").decode()
        )
        self.address = Address.from_public_key_hex(self.public_key)

    def sign(self, message: str, encoding="base64"):
        return self.signing_key.sign(message.encode(), encoding=encoding)


def verify_signature(
    public_key_hex: str, signature: str, message: str, encoding="base64"
):
    verifying_key = ed25519.VerifyingKey(public_key_hex, encoding="hex")
    verifying_key.verify(signature.encode(), message.encode(), encoding=encoding)
