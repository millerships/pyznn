---
sidebar_position: 4
---

# Wallet

## Create wallet from mnemonic

```python
from znn.wallet.keystore import KeyStore

MNEMONIC = (
    "route become dream access impulse price inform obtain engage ski believe awful "
    "absent pig thing vibrant possible exotic flee pepper marble rural fire fancy"
)

keystore = KeyStore(MNEMONIC)

print(keystore.seed)
# Out: 19f1d107d49f42ebc14d46b51001c731569f142590fdd20167ddeedbb201516731ad5ac9b58d3a1c9c09debfe62538379461e4ea9f038124c428784fecc645b7

kp = keystore.get_key_pair(0)  # `0` is default btw, so no need to pass it, just being explicit here for the sake of the example

print(kp.private_key)
# Out: d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863

print(str(kp.address))
# Out: z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7
```

Following BIP44, `m / purpose' / coin_type' / account' / change / address_index`, you can get keypairs for other account indices as well.

For example, `kp = keystore.get_key_pair(1)` works.

## Get Keypair from PrivateKey

```python
from znn.wallet.keypair import KeyPair

keypair = KeyPair("d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863")

print(str(keypair.address))
# Out: z1qqjnwjjpnue8xmmpanz6csze6tcmtzzdtfsww7
```

## Signing and verifying a message

```python
from znn.wallet.keypair import KeyPair
from znn.wallet.keypair import verify_signature

keypair = KeyPair("d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863")

signed_msg = keypair.sign("Hello, aliens")
verify_signature(keypair.public_key, signed_msg.decode(), "Hello, aliens")
```

Verification throws `BadSignatureError` if it fails.

## Send transaction

Wallet module comes with a `Transact` class that helps with sending/publishing a transaction.

Here's an example.

```python
from znn.wallet.transact import Transact
from znn.model.primitives.address import Address
from znn.model.primitives.token_standard import ZNN_ZTS

# Transact's init method expects the private_key of the account you want to use for signing
tx = Transact("d6b01f96b566d7df9b5b53b1971e4baeb74cc64167a9843f82d04b2194ca4863")

to_address = Address.parse("z1qzpcwr6lk0zhejzpt04j2jcqqadtu046ffr8nr")
await tx.send(to, ZNN_ZTS, 100000000)
```
