from dragonion_core.proto.web.webmessage import WebConnectionMessage

from dragonion.modules.tui.chat.widgets.containers import MessagesContainer

from .helpers import render_time


async def handle_connect(webmessage: WebConnectionMessage):
    from dragonion.modules.tui import app

    container = app.query_one(MessagesContainer)

    app.user_storage.keys |= {webmessage.username: webmessage.public_key}
    container.write(
        f"- Connected {webmessage.username} - " f"{render_time(webmessage.time)}"
    )
