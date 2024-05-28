from textual import on
from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Button, Input, LoadingIndicator, Static

from .inputs import UsernameInputLayout


class GenerateIdentityContainer(Static):
    DEFAULT_CSS = """
    #generate_identity_button {
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Center(UsernameInputLayout())
        yield Center(
            Button(
                label="Generate identity",
                name="generate_identity_button",
                variant="success",
                id="generate_identity_button",
                disabled=True,
            )
        )

    @on(Button.Pressed, "#generate_identity_button")
    @on(Input.Submitted, "#username_input")
    def on_generate_button_pressed(self, _: Button.Pressed):
        """
        On generate button press
        :param _:
        :return: Modifies global app.identity to generated
        """
        try:
            from dragonion_core.proto.encryption.identity import Identity

            from ... import app

            app.query_one("IdentityWidget").remove()
            app.mount(LoadingIndicator())

            if _username := self.query_one("#username_input", expect_type=Input).value:
                app.identity = Identity(username=_username)
        except Exception as e:
            assert e
            from ... import app

            app.bell()
