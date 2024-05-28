from textual.widgets import Input

from .command.command import handle_command
from .message import handle_message


async def handle_input_submit():
    from dragonion.modules.tui import app

    field = app.query_one("#chat_input_field", expect_type=Input)
    message = field.value
    if len(message) == 0:
        return
    field.value = ""

    if message[0] == "/":
        await handle_command(message)
    else:
        await handle_message(message)
