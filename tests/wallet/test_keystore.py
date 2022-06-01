from znn.wallet.keystore import KeyStore


MNEMONIC = (
    "route become dream access impulse price inform obtain engage ski believe awful "
    "absent pig thing vibrant possible exotic flee pepper marble rural fire fancy"
)
SEED_HEX = (
    "19f1d107d49f42ebc14d46b51001c731569f142590fdd20167ddeedbb201516731ad5ac9b"
    "58d3a1c9c09debfe62538379461e4ea9f038124c428784fecc645b7"
)
ENTROPY_HEX = "bc827d0a00a72354dce4c44a59485288500b49382f9ba88a016351787b7b15ca"


class TestKeyStore:
    def test_get_key_pair_derive_address_0(self):
        expected_address = "z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7"
        keystore = KeyStore(MNEMONIC)

        assert keystore.seed == SEED_HEX
        assert keystore.entropy == ENTROPY_HEX

        acc_privkey_hex = (
            "d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863"
        )
        kp = keystore.get_key_pair(0)
        assert kp.private_key == acc_privkey_hex
        assert str(kp.address) == expected_address

    def test_get_key_pair_derive_address_1(self):
        expected_address = "z1qr44l6ajstm5gfrvwtsrfg446y6mcv8r60v090"
        keystore = KeyStore(MNEMONIC)

        acc_privkey_hex = (
            "bd14c955a2e67246dd8f273127a124ef97b869ef1301378c44760f96b426ee18"
        )
        kp = keystore.get_key_pair(1)
        assert kp.private_key == acc_privkey_hex
        assert str(kp.address) == expected_address

    def test_get_key_pair_derive_address_70000(self):
        expected_address = "z1qrjky0nhej0pfldk7a23v6yayx9l26rss3ghcy"
        keystore = KeyStore(MNEMONIC)

        acc_privkey_hex = (
            "e5edac32c406d07c1b40adfb7aa12cc6bc788632da4c7aedb3e506d4a733664d"
        )
        kp = keystore.get_key_pair(70000)
        assert kp.private_key == acc_privkey_hex
        assert str(kp.address) == expected_address

    def test_new_random(self):
        keystore = KeyStore.new_random()
        kp = keystore.get_key_pair(0)
        assert len(str(kp.address)) == 40
