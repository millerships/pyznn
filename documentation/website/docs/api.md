---
sidebar_position: 3
---

# Built-in APIs

The package comes with utility access to storage blocks through various methods.

## List of all the APIs

- Ledger
- Stats (node stats)
- Embedded endpoints
  - Accelerator
  - Pillar
  - Plasma
  - Sentinel
  - Stake
  - Swap
  - Token

## Examples

### Ledger

```python
from znn.api.ledger import LedgerApi

ledger = LedgerApi()
await ledger.get_account_info_by_address("z1qpa4flg6m7r27rvpyturavecmemkxh7ms8vrp7")
```

Example output

```python
{'address': 'z1qpa4flg6m7r27rvpyturavecmemkxh7ms8vrp7',
 'accountHeight': 2,
 'balanceInfoMap': {'zts1znnxxxxxxxxxxxxx9z4ulx': {'token': {'name': 'ZNN',
    'symbol': 'ZNN',
    'domain': 'zenon.network',
    'totalSupply': 821070711786609,
    'decimals': 8,
    'owner': 'z1qxemdeddedxt0kenxxxxxxxxxxxxxxxxh9amk0',
    'tokenStandard': 'zts1znnxxxxxxxxxxxxx9z4ulx',
    'maxSupply': 9007199254740991,
    'isBurnable': True,
    'isMintable': True,
    'isUtility': True},
   'balance': 200000000}}}
```

### Stats

```python
from znn.api.stats import StatsApi

stats = StatsApi()
await stats.os_info()
```

Example output

```python
{'os': 'linux',
 'platform': 'ubuntu',
 'platformFamily': 'debian',
 'platformVersion': '20.04',
 'kernelVersion': '5.13.0-1031-aws',
 'memoryTotal': 16777953280,
 'memoryFree': 3140345856,
 'numCPU': 4,
 'numGoroutine': 989311}
```

### Subscribe

```python
from znn.api.subscribe import SubscribeApi

s = SubscribeApi()
await s.to_all_account_blocks()
```

This listens to incoming messages and produces a stream of output.

Example output

```python
{"jsonrpc":"2.0","id":4,"result":"0xe1e9e9c83252c5c27064ba5b1d8d1084"}

{"jsonrpc":"2.0","method":"ledger.subscription","params":{"subscription":"0xe1e9e9c83252c5c27064ba5b1d8d1084","result":[{"blockType":3,"hash":"eb7ce3131fbed736533efbad2d2558048f0ad3fcacc10c58b027398015ba0f77","height":488,"address":"z1qqznc455h9lfy3pa9dhvr79f86xjsgredgnccx","toAddress":"z1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsggv2f","fromHash":"65a2d0ada9809e1c49c406c433d95acbb03a2d15abd7d522e7c1f246dafbff17"},{"blockType":3,"hash":"44a22f6bc85f7b930a897d343c36e4c15ba2a7f78318282f0cf082a5e3d7450d","height":372,"address":"z1qphdard896khmydq86fw2mshq8r7zc7wg3lujs","toAddress":"z1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsggv2f","fromHash":"6e103fed49bbf1be693d793e089edae9bed66e90356355e7d15c793a2b8a1e36"},{"blockType":3,"hash":"25be320b369e241b5dc63a712d9b1591a5c3eeef8f519b5aeba26fdbb5e5cc9b","height":373,"address":"z1qphdard896khmydq86fw2mshq8r7zc7wg3lujs","toAddress":"z1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsggv2f","fromHash":"da42c0a3baec2220e811b60b15f412f5a3f03995dc26b3069a4412b9ab6043de"}]}}

```
