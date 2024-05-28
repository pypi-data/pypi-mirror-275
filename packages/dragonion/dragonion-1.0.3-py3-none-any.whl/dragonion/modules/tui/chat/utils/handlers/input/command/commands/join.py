import asyncio

import websockets.client
from dragonion_core.proto.web.webmessage import WebConnectionMessage, WebMessage

from dragonion.modules.tui.chat.utils.tasks.socket_handler.task import handle_websocket


async def join_command(command_args: list):
    command_args.append("None")
    if command_args[0] == "None":
        return "you need to specify room name"

    from dragonion.modules.tui import app

    log = app.query_one("MessagesContainer")

    if not app.user_storage.sock:
        log.write("[red]Error[/]: run /connect command first")
        return

    if app.user_storage.websocket:
        log.write("[green]Disconnecting from room...[/]")
        await app.user_storage.websocket.close()
        await app.user_storage.websocket.wait_closed()
        app.user_storage.sock.close()
        from socks import GeneralProxyError

        from .helpers import socket

        try:
            socket.connect()
        except GeneralProxyError:
            log.write(
                f"Cannot reach service, it may be turned off or you have "
                f"irrelevant id-key pair (auth file)"
            )
            return

    log.write(f"[green]Connecting to {command_args[0]}...")
    app.user_storage.websocket = await websockets.client.connect(
        f"ws://{app.user_storage.host}:80/{command_args[0]}", sock=app.user_storage.sock
    )
    await app.user_storage.websocket.send(
        WebConnectionMessage(
            username=app.identity.username,
            public_key=app.identity.public_key(),
            password=command_args[1],
        ).to_json()
    )

    connection_message = WebMessage.from_json(await app.user_storage.websocket.recv())

    if connection_message.type == "error":
        log.write(
            f"[red]Error connecting to room[/]: {connection_message.error_message}"
        )
    elif connection_message.type == "connect_answer":
        app.user_storage.keys = connection_message.connected_users
        asyncio.create_task(handle_websocket())
    else:
        log.write(
            f"Received unknown answer {connection_message.type}: {connection_message}"
        )
