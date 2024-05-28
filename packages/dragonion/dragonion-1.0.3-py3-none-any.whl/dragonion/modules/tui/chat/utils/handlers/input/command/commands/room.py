async def room_command(command_args: list):
    if command_args:
        return "this command doesn't accepts any arguments"

    from dragonion.modules.tui import app

    container = app.query_one("MessagesContainer")

    if app.user_storage.keys:
        container.write("[green]Connected users[/]")
        container.write("\n".join(app.user_storage.keys.keys()))
    else:
        container.write("You aren't connected to any room")
