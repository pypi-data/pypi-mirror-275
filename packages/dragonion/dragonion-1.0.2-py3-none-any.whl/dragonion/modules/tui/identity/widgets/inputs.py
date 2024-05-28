from textual import on
from textual.app import ComposeResult
from textual.validation import Length
from textual.widgets import Button, Input, Static


class UsernameInputLayout(Static):
    DEFAULT_CSS = """
    #username_input {
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(
            placeholder="username",
            id="username_input",
            validators=[
                Length(
                    minimum=4,
                    maximum=14,
                    failure_description="Username length must be from 4 to 14 symbols",
                )
            ],
        )

    @on(Input.Changed, "#username_input")
    def on_username_validate(self, event: Input.Changed):
        from ... import app

        app.query_one(
            "#generate_identity_button", expect_type=Button
        ).disabled = not event.validation_result.is_valid
