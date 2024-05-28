from dragonion_core.proto.encryption.identity import Identity
from textual.app import ComposeResult
from textual.widgets import Static

from ..authentication.utils.results import ServiceAuthResult
from .widgets.containers import MessagesContainer
from .widgets.inputs.message_input import InputContainer


class ChatWidget(Static):
    DEFAULT_CSS = """
    .input {
        dock: bottom;
        height: 3;
    }
    """

    def __init__(self, service_auth: ServiceAuthResult, identity: Identity):
        self.service_auth = service_auth
        self.identity = identity
        super().__init__()

    def _on_compose(self) -> None:
        from .. import app

        # noinspection PyTypeChecker
        app.title = "dragonion"

    def compose(self) -> ComposeResult:
        yield MessagesContainer()
        yield InputContainer()
