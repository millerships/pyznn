from znn.embedded.definitions import PILLAS_ABI
from znn.embedded.definitions import STAKE_ABI
from znn.embedded.definitions import TOKEN_ABI
from znn.model.primitives.token_standard import ZNN_ZTS


class TestABI:
    def test_stake_abi_encode_and_decode(self):
        value = "0x1234567812345678123456781234567812345678123456781234567812345678"
        encoded_bytes = STAKE_ABI.encode("Cancel", [value])
        expected_encoded_hex = "5a92fe321234567812345678123456781234567812345678123456781234567812345678"  # noqa
        assert expected_encoded_hex == encoded_bytes.hex()

        expected_decoded = {"id": value}
        decoded = STAKE_ABI.decode("Cancel", encoded_bytes)
        assert decoded == expected_decoded

    def test_token_abi_issue_token_encode_and_decode(self):
        data = {
            "tokenName": "Really long text which is more than 32 bytes",
            "tokenSymbol": "kinda short text",
            "tokenDomain": "what is this text does it ever end?01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789",  # noqa
            "totalSupply": 100192674782882803782,
            "maxSupply": 1000000000000000000,
            "decimals": 123,
            "isMintable": True,
            "isBurnable": False,
            "isUtility": True,
        }
        encoded_bytes = TOKEN_ABI.encode(
            "IssueToken",
            [
                data["tokenName"],
                data["tokenSymbol"],
                data["tokenDomain"],
                100192674782882803782,
                1000000000000000000,
                data["decimals"],
                data["isMintable"],
                data["isBurnable"],
                data["isUtility"],
            ],
        )
        expected_encoded_hex = "bc410b910000000000000000000000000000000000000000000000000000000000000120000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001c00000000000000000000000000000000000000000000000056e73e2df19f7b0460000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000000000000000000000007b000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000002c5265616c6c79206c6f6e672074657874207768696368206973206d6f7265207468616e203332206279746573000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000106b696e64612073686f72742074657874000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000091776861742069732074686973207465787420646f6573206974206576657220656e643f3031323334353637383930313233343536373839303132333435363738393031323334353637383930313233343536373839303132333435363738393031323334353637383930313233343536373839303132333435363738393031323334353637383930313233343536373839000000000000000000000000000000"  # noqa
        assert expected_encoded_hex == encoded_bytes.hex()

        decoded = TOKEN_ABI.decode("IssueToken", encoded_bytes)
        assert decoded == data

    def test_token_abi_mint_encode_and_decode(self):
        token_standard = ZNN_ZTS
        amount = 123456789
        receiver = "z1qp5hmcddaxd8ranhu25n4nycf8q9vsg6ksqjlg"
        encoded_bytes = TOKEN_ABI.encode("Mint", [token_standard, amount, receiver,])
        expected_encoded_hex = "cd70f9bc0000000000000000000000000000000000000000000014e66318c6318c6318c600000000000000000000000000000000000000000000000000000000075bcd1500000000000000000000000000697de1ade99a71f677e2a93acc9849c056411a"  # noqa
        assert expected_encoded_hex == encoded_bytes.hex()

        decoded = TOKEN_ABI.decode("Mint", encoded_bytes)
        expected_decoded = {
            "tokenStandard": str(ZNN_ZTS),
            "amount": amount,
            "receiveAddress": receiver,
        }
        assert decoded == expected_decoded

    def test_pillar_register_encode_and_decode(self):
        data = {
            "name": "Really long text which is more than 32 bytes",
            "producerAddress": "z1qp5hmcddaxd8ranhu25n4nycf8q9vsg6ksqjlg",
            "rewardAddress": "z1qp5hmcddaxd8ranhu25n4nycf8q9vsg6ksqjlg",
            "giveBlockRewardPercentage": 50,
            "giveDelegateRewardPercentage": 75,
        }
        encoded_bytes = PILLAS_ABI.encode(
            "Register",
            [
                data["name"],
                data["producerAddress"],
                data["rewardAddress"],
                data["giveBlockRewardPercentage"],
                data["giveDelegateRewardPercentage"],
            ],
        )
        expected_encoded_hex = "644de92700000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000697de1ade99a71f677e2a93acc9849c056411a00000000000000000000000000697de1ade99a71f677e2a93acc9849c056411a0000000000000000000000000000000000000000000000000000000000000032000000000000000000000000000000000000000000000000000000000000004b000000000000000000000000000000000000000000000000000000000000002c5265616c6c79206c6f6e672074657874207768696368206973206d6f7265207468616e2033322062797465730000000000000000000000000000000000000000"  # noqa
        assert expected_encoded_hex == encoded_bytes.hex()

        decoded = PILLAS_ABI.decode("Register", encoded_bytes)
        assert decoded == data
