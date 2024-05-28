from dragonion_core.proto.web.webmessage import WebErrorMessage

from dragonion.modules.tui.chat.widgets.containers import MessagesContainer

from .helpers import render_time


async def handle_error(webmessage: WebErrorMessage):
    from dragonion.modules.tui import app

    container = app.query_one(MessagesContainer)

    container.write(
        f"[red]- {webmessage.error_message} - " f"{render_time(webmessage.time)}[/]"
    )
