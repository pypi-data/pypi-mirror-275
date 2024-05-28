from dragonion_core.proto.web.webmessage import WebMessageMessage

from dragonion.modules.tui.chat.widgets.containers import MessagesContainer
from dragonion.modules.tui.chat.widgets.items.message import Message


async def handle_message(webmessage: WebMessageMessage):
    from dragonion.modules.tui import app

    container = app.query_one(MessagesContainer)

    if (
        not container.last_message
        or container.last_message.author != webmessage.username
    ):
        container.mount_scroll_adaptive(
            Message(
                avatar=webmessage.avatar,
                message=webmessage.decrypt(app.identity),
                author=webmessage.username,
                time=webmessage.time,
            )
        )
    else:
        container.last_message.add_message(
            message=webmessage.decrypt(app.identity), time=webmessage.time
        )
