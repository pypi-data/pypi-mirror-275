from textual import on
from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Button, Input, Label, Select, Static

from ..utils.results import ServiceAuthResult
from .inputs import AuthFileSelect, RawStringsAuthLayout


class AuthVariants(Static):
    DEFAULT_CSS = """
    .margin-1 {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield AuthFileSelect()
        yield Center(Label("OR", classes="margin-1"))
        yield RawStringsAuthLayout()

    @on(Input.Changed)
    def on_input_changed(self):
        """
        Disable and enable file select on raw strings input changed
        :return:
        """
        if (
            self.query_one("#login_auth_string_input", expect_type=Input).value
            or self.query_one("#login_service_id_input", expect_type=Input).value
        ):
            self.query_one(AuthFileSelect).disabled = True
        else:
            self.query_one(AuthFileSelect).disabled = False

    @on(Select.Changed)
    def on_select_changed(self, event: Select.Changed):
        """
        Disable and enable raw strings on file input changed
        :param event: Event passed by decorator
        :return:
        """
        if event.value:
            self.query_one(
                "#login_auth_string_input", expect_type=Input
            ).disabled = True
            self.query_one("#login_service_id_input", expect_type=Input).disabled = True
        else:
            self.query_one(
                "#login_auth_string_input", expect_type=Input
            ).disabled = False
            self.query_one(
                "#login_service_id_input", expect_type=Input
            ).disabled = False


class LoginContainer(Static):
    DEFAULT_CSS = """
    #login_authenticate_button {
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Center(AuthVariants())
        yield Center(
            Button(
                label="Authenticate",
                name="authenticate_button",
                variant="success",
                id="login_authenticate_button",
            )
        )

    @on(Button.Pressed, "#login_authenticate_button")
    def on_auth_button_pressed(self, _: Button.Pressed):
        """
        On auth button press
        :param _:
        :return: Modifies global app.service_auth to service auth result where one of
                 params is None, and other has validated value
        """
        try:
            from ... import app

            app.service_auth = ServiceAuthResult(
                raw_auth_strings=(
                    (
                        _service_id := self.query_one(
                            "#login_service_id_input", expect_type=Input
                        ).value
                    ),
                    (
                        _auth_string := self.query_one(
                            "#login_auth_string_input", expect_type=Input
                        ).value
                    ),
                ),
                service_auth_file=self.query_one(Select).value,
            )
        except Exception as e:
            assert e
            from ... import app

            app.bell()
