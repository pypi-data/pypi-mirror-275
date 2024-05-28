from dataclasses import dataclass, field

import websockets.client
from socks import socksocket

from dragonion.utils.core.emoji import random_emoji
from dragonion.utils.onion import Onion


@dataclass
class UserStorage:
    avatar: str = random_emoji()
    keys: dict[str, bytes] = field(default_factory=dict)
    host: str = None
    onion: Onion = None
    sock: socksocket = None
    websocket: websockets.client.WebSocketClientProtocol = None
    connect: bool = False
    dev_proxy_port: int = None
