from datetime import datetime

from textual import events
from textual.app import ComposeResult
from textual.widgets import Label, Static


class Avatar(Static):
    DEFAULT_CSS = """
    Avatar {
        width: auto;
    }
    """

    def __init__(self, symb: str):
        self.symb = symb
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(f"({self.symb}) ")


class MessageHeader(Static):
    DEFAULT_CSS = """
    MessageHeader {
        layout: horizontal;
        background: $boost;
        width: auto;
    }
    """

    def __init__(self, message: str, time: datetime):
        self.message = message
        self.time = time
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(f"[bold]{self.message}[/]")
        yield Label(" ")
        yield Label(f"[#a5abb3][{self.time.time().strftime('%H:%M:%S')}][/]")


class MessageContent(Static):
    DEFAULT_CSS = """
    MessageContent {
        layout: horizontal;
        width: 1fr;
        height: auto;
    }
    
    ._message_content_text {
        width: auto;
        height: auto;
        margin-right: 5;
    }
    
    .message_time {
        height: auto;
        offset-x: -3;
    }
    """

    def __init__(self, message: str, time: datetime):
        self.message = message
        self.time = time
        super().__init__()

    def _on_mount(self, event: events.Mount) -> None:
        self.query_one(".message_time").visible = False

    def _on_enter(self, event: events.Focus) -> None:
        self.query_one(".message_time").visible = True

    def _on_leave(self, event: events.Blur) -> None:
        self.query_one(".message_time").visible = False

    def compose(self) -> ComposeResult:
        yield Static(self.message, classes="_message_content_text", shrink=True)
        yield Static(
            f"[#a5abb3][{self.time.time().strftime('%H:%M:%S')}][/]",
            classes="message_time",
        )


class TextMessage(Static):
    DEFAULT_CSS = """
    TextMessage {
        layout: vertical;
        width: auto;
    }
    """

    def __init__(self, author: str, message: str, time: datetime):
        self.author = author
        self.message = message
        self.time = time
        super().__init__()

    def compose(self) -> ComposeResult:
        yield MessageHeader(self.author, self.time)
        yield MessageContent(self.message, self.time)


class Message(Static):
    DEFAULT_CSS = """
    Message {
        layout: horizontal;
        margin-bottom: 1;
        height: auto;
    }
    """

    def __init__(self, avatar: str, author: str, message: str, time: datetime):
        self.avatar = avatar
        self.author = author
        self.message = message
        self.time = time
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Avatar(symb=self.avatar)
        yield TextMessage(author=self.author, message=self.message, time=self.time)

    def add_message(self, message: str, time: datetime):
        self.query_one(TextMessage).mount(m := MessageContent(message, time))
        self.app.query_one("MessagesContainer").scroll_adaptive_to(m)
