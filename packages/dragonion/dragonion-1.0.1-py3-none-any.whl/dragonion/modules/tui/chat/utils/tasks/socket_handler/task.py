import websockets.exceptions
from dragonion_core.proto.web.webmessage import WebMessage

from dragonion.modules.tui.chat.widgets.containers import MessagesContainer

from .handlers import (
    handle_connect,
    handle_disconnect,
    handle_error,
    handle_message,
    handle_notification,
)


async def unknown_message(_):
    pass


async def handle_websocket():
    from dragonion.modules.tui import app

    container = app.query_one(MessagesContainer)

    async for message in app.user_storage.websocket:
        try:
            webmessage = WebMessage.from_json(message)

            await (
                {
                    "connect": handle_connect,
                    "disconnect": handle_disconnect,
                    "message": handle_message,
                    "notification": handle_notification,
                    "error": handle_error,
                }.get(webmessage.type, unknown_message)(webmessage)
            )

        except websockets.exceptions.ConnectionClosedOK:
            pass
        except websockets.exceptions.ConnectionClosed:
            container.write(f"[bold red]Disconnected[/], consider rejoining")
        except Exception as e:
            container.write(f"[red]Error {e.__class__}[/] in message handler: {e}")
