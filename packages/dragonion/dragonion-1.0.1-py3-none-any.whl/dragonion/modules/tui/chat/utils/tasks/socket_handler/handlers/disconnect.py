from dragonion_core.proto.web.webmessage import WebDisconnectMessage

from dragonion.modules.tui.chat.widgets.containers import MessagesContainer

from .helpers import render_time


async def handle_disconnect(webmessage: WebDisconnectMessage):
    from dragonion.modules.tui import app

    container = app.query_one(MessagesContainer)

    container.write(
        f"- Disconnected {webmessage.username} - " f"{render_time(webmessage.time)}"
    )
