from dragonion_core.proto.web.webmessage import WebNotificationMessage

from dragonion.modules.tui.chat.widgets.containers import MessagesContainer

from .helpers import render_time


async def handle_notification(webmessage: WebNotificationMessage):
    from dragonion.modules.tui import app

    container = app.query_one(MessagesContainer)

    container.write(
        f"[blue]- {webmessage.message} - " f"{render_time(webmessage.time)}[/]"
    )
