from textual.widgets import Static

from .commands.avatar import avatar_command
from .commands.connect import connect_command
from .commands.disconnect import disconnect_command
from .commands.exit import exit_command
from .commands.help import help_command
from .commands.join import join_command
from .commands.room import room_command


async def not_found_command(_: list):
    from dragonion.modules.tui import app

    app.query_one("MessagesContainer").write(
        "[red]Command not found[/], use /help to get list of available commands"
    )


async def handle_command(full_text: str):
    command, args = (full_text.partition(" ")[0], full_text.partition(" ")[2].split())

    try:
        result = await (
            {
                "/help": help_command,
                "/join": join_command,
                "/connect": connect_command,
                "/disconnect": disconnect_command,
                "/avatar": avatar_command,
                "/room": room_command,
                "/exit": exit_command,
            }.get(command, not_found_command)(args)
        )
    except Exception as e:
        result = f"{e.__class__}: {e}"

    if result is not None:
        from dragonion.modules.tui import app

        app.query_one("MessagesContainer").mount_scroll(
            Static(f"[red]Error[/] happened while executing {command}: " f"{result} \n")
        )
