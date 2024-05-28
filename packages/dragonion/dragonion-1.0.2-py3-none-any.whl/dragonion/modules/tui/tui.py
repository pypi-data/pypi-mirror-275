import asyncio

from dragonion_core.proto.encryption.identity import Identity
from ezzthread import threaded
from textual.app import App, ComposeResult
from textual.css.query import NoMatches
from textual.reactive import reactive
from textual.widgets import Header, LoadingIndicator

from .authentication import authentication
from .authentication.utils.results import ServiceAuthResult
from .chat import chat
from .helpers.storage import UserStorage
from .identity import identity


class DragonionTuiApp(App):
    _pre_service_auth = None
    _pre_username = None
    service_auth = reactive(None)
    identity = reactive(None)
    user_storage = UserStorage()

    def compose(self) -> ComposeResult:
        yield Header()
        if not self._pre_service_auth:
            yield authentication.LoginWidget()

    def _on_compose(self) -> None:
        if self._pre_service_auth is not None:
            self.service_auth = self._pre_service_auth

    def watch_service_auth(self):
        if isinstance(self.service_auth, ServiceAuthResult):
            try:
                self.query_one(authentication.LoginWidget).remove()
            except NoMatches:
                pass

            if self._pre_username:
                self.mount(LoadingIndicator())
                self.identity = Identity(self._pre_username)
            else:
                self.mount(identity.IdentityWidget())

    async def watch_identity(self):
        if isinstance(self.identity, Identity):
            try:
                threaded(self.identity.generate)()
                while self.identity.private_key is None:
                    await asyncio.sleep(0.1)
                await self.query_one(LoadingIndicator).remove()
            except NoMatches:
                pass

            if (
                self.identity
                and isinstance(self.service_auth, ServiceAuthResult)
                and len(list(self.query("ChatWidget").results())) == 0
            ):
                await self.mount(
                    chat.ChatWidget(
                        service_auth=self.service_auth, identity=self.identity
                    )
                )
                if self.user_storage.connect:
                    from .chat.utils.handlers.input.command.commands.connect import (
                        connect_command,
                    )

                    await connect_command(list())

    def _on_exit_app(self) -> None:
        if self.user_storage.onion:
            self.user_storage.onion.cleanup()


app = DragonionTuiApp()
