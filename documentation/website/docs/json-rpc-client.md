---
sidebar_position: 2
---

# JSON-RPC client

Supported clients:

- Websocket

HTTP is in the "good to have" list.

## Initiate a websocket connection

```python
from znn.client.websocket import WsClient

ws = WsClient("ws://nodes.zenon.place:35998")
```

You can either run your own node or connect to publicly available node. There are a bunch of publicly available nodes listed at the end of this page.

There's also one helper function to get a Websocket client that connects to above node by default.

```python
from znn.client.websocket import get_default_client

ws = get_default_client()
```

## Sending requests

Let's take an example.

### Get account info by address

```python
from znn.client.websocket import WsClient

ws = WsClient("ws://nodes.zenon.place:35998")
await ws.send_request("ledger.getAccountInfoByAddress", ["z1qpa4flg6m7r27rvpyturavecmemkxh7ms8vrp7"])
```

## Listening to incoming messages

You can subscribe to incoming messages. Let's take another example.

### Subscribe to all account blocks

```python

from znn.client.websocket import get_default_client

ws = get_default_client()
ws.send_and_listen("ledger.subscribe", ["allAccountBlocks"])
```

That should start spitting messages in a few seconds.

## List of publicly available nodes

```
ws://public.deeZNNodez.com:35998
ws://node01.0x3639.com:35998
ws://node02.0x3639.com:35998
ws://node03.0x3639.com:35998
ws://chadasscapital.com:35998
ws://nodes.zenon.place:35998
ws://node01.nodez.space:35998
ws://node02.nodez.space:35998
ws://node03.nodez.space:35998
wss://ssl.deeZNNodez.com:35998
```
