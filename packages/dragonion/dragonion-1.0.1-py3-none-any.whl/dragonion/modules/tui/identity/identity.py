from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Static

from .widgets.containers import GenerateIdentityContainer


class IdentityWidget(Static):
    DEFAULT_CSS = """
    IdentityWidget {
        height: 100%;
        layout: vertical;
        align-vertical: middle;
    }

    GenerateIdentityContainer {
        align: center middle; 
        height: 1fr;
        max-width: 50%;
    }
    """

    def _on_compose(self) -> None:
        from .. import app

        # noinspection PyTypeChecker
        app.title = "dragonion - identity"

    def compose(self) -> ComposeResult:
        yield Center(GenerateIdentityContainer())
