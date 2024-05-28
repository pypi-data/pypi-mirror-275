from dataclasses import dataclass

from textual.widgets import Static


@dataclass
class CommandHelp:
    short_description: str
    args_description: dict | None
    long_description: str


async def help_command(command_args: list):
    from dragonion.modules.tui import app

    container = app.query_one("MessagesContainer")

    commands = {
        "help": CommandHelp(
            short_description="Get help",
            args_description={"command": "Command name to get info about"},
            long_description="Show this message or pass name of any existing command "
            "to get info about it",
        ),
        "join": CommandHelp(
            short_description="Join room",
            args_description={
                "name": "Name of room to join",
                "password": "Room password, combination of same room name and password "
                "will unite two or more users in one room. Entering "
                "password, that is different from other room members "
                "will lead you to connecting to ANOTHER room!",
            },
            long_description="Join room, pass room name to join with default password "
            "or pass room name and password split with space to join "
            "password-locked room.",
        ),
        "connect": CommandHelp(
            short_description="Connect to network",
            long_description="Start tor service and connect to it",
            args_description=None,
        ),
        "disconnect": CommandHelp(
            short_description="Disconnect from room",
            long_description="Will disconnect you from room and close current "
            "onion network connection, you need to rejoin room to"
            "continue using chat",
            args_description=None,
        ),
        "avatar": CommandHelp(
            short_description="Set avatar",
            long_description="Will generate random avatar if no symbol specified "
            "or will set your avatar to specified symbol",
            args_description={
                "symbol": "Must be exactly 1 character or not specified, avatar will "
                "be set to this character."
            },
        ),
        "room": CommandHelp(
            short_description="Get users",
            long_description="Will return list of users in your room (you will be in"
            "list also)",
            args_description=None,
        ),
        "exit": CommandHelp(
            short_description="Exit chat",
            long_description="Closes connection and leaves application",
            args_description=None,
        ),
    }

    if command_args:
        help_ = commands.get(command_args[0])
        if help_ is None:
            return f"command {command_args[0]} doesn't exist"
        container.write(f"[green]/{command_args[0]}[/] command: ")
        container.write(help_.long_description)
        if help_.args_description is None:
            return
        container.write("[gray]Arguments:[/] ")
        for arg in help_.args_description.keys():
            container.mount_scroll(
                Static(f"[italic]{arg}[/]\t{help_.args_description[arg]}")
            )

    else:
        for cmd in commands.keys():
            container.mount_scroll(Static(f"/{cmd}\t{commands[cmd].short_description}"))
