import os

from textual.app import ComposeResult
from textual.widgets import Input, Select, Static


class AuthFileSelect(Static):
    def compose(self) -> ComposeResult:
        yield Select(
            ((file, file) for file in os.listdir() if file.endswith(".auth")),
            prompt="Service .auth file",
            id="auth_file_select",
        )


class RawStringsAuthLayout(Static):
    DEFAULT_CSS = """
    #login_auth_string_input {
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(placeholder="service id", id="login_service_id_input")
        yield Input(
            placeholder="AUTH STRING", id="login_auth_string_input", password=True
        )
