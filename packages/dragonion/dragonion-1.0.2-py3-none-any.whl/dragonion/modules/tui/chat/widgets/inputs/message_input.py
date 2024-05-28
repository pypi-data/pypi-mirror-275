from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Input

from ...utils.handlers.input.general import handle_input_submit


class InputContainer(Horizontal):
    DEFAULT_CSS = """
    .input_field {
        width: 1fr;
        border: tall $accent;
    }
    .input_submit {
        min-width: 7;
        width: 7;
    }
    """

    def compose(self) -> ComposeResult:
        self.classes = "input"

        yield Input(classes="input_field", id="chat_input_field")
        yield Button(
            ">",
            classes="input_submit",
            variant="primary",
            id="chat_input_submit_button",
        )

    @on(Button.Pressed, "#chat_input_submit_button")
    @on(Input.Submitted, "#chat_input_field")
    async def on_submit(self):
        await handle_input_submit()
