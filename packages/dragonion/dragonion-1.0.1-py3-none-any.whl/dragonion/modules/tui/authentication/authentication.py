from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Static

from .widgets.containers import LoginContainer


class LoginWidget(Static):
    DEFAULT_CSS = """
    LoginWidget {
        height: 100%;
        layout: vertical;
        align-vertical: middle;
    }

    LoginContainer {
        align: center middle; 
        height: 1fr;
        max-width: 50%;
    }
    """

    def _on_compose(self) -> None:
        from .. import app

        # noinspection PyTypeChecker
        app.title = "dragonion - authentication"

    def compose(self) -> ComposeResult:
        yield Center(LoginContainer())
