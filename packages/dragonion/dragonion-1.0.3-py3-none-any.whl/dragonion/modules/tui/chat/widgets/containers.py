import textwrap

from textual import events
from textual.containers import ScrollableContainer
from textual.css.query import NoMatches
from textual.widget import Widget
from textual.widgets import Static

from .items.message import Message


class MessagesContainer(ScrollableContainer):
    DEFAULT_CSS = """
    MessagesContainer {
        padding: 1;
        width: 1fr;
        height: 1fr;
        margin-left: 1;
    }
    
    .dragonion_help_logo {
        content-align: center top;
        align-horizontal: center;
        width: 1fr;
        height: auto;
    }
    """

    def _on_mount(self, event: events.Mount) -> None:
        self.mount(
            Static(
                textwrap.dedent(
                    """\
            ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗██╗ ██████╗ ███╗   ██╗
            ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██║██╔═══██╗████╗  ██║
            ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║██║██║   ██║██╔██╗ ██║
            ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██║██║   ██║██║╚██╗██║
            ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║╚██████╔╝██║ ╚████║
            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                    Most modern-looking, encrypted and functional in-console
                                onion chat that you control! 
            Use /connect command to establish onion connection, than /join to connect 
                    to room or /help to get list of all available commands          
                """
                ),
                classes="dragonion_help_logo",
            ),
        )

    def write(self, text: str, classes: str = "", _id: str = None, no_newline=False):
        self.mount(
            w := Static(
                text + ("\n" if not no_newline else ""),
                classes=classes,
                id=_id,
                shrink=True,
            )
        )
        w.scroll_visible(duration=1)

    def mount_scroll(self, widget: Widget):
        self.mount(widget)
        widget.scroll_visible(duration=1)

    def mount_scroll_adaptive(self, widget: Widget):
        self.mount(widget)
        self.scroll_adaptive_to(widget)

    def scroll_adaptive_to(self, widget: Widget):
        """
        Scrolls to specified widget if user didn't scroll up
        :param widget:
        :return:
        """
        if self.scroll_offset.y == self.max_scroll_y:
            widget.scroll_visible(duration=1)

    @property
    def last_message(self) -> Message | None:
        try:
            widget = self.query(None).last()
            if "message_time" in widget.classes:
                # noinspection PyTypeChecker
                return self.query(Message).last()
            else:
                return None
        except NoMatches:
            return None
