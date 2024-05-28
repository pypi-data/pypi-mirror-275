from textual.widgets import Static


async def disconnect_command(command_args: list):
    if command_args:
        return "this command doesn't accepts any arguments"

    from dragonion.modules.tui import app

    container = app.query_one("MessagesContainer")

    if app.user_storage.websocket:
        container.write("[green]Disconnecting from room...[/]")
        await app.user_storage.websocket.close()
        await app.user_storage.websocket.wait_closed()
        app.user_storage.sock.close()
        app.user_storage.keys = {}

    if onion := app.user_storage.onion:
        onion.cleanup()

    container.mount_scroll(Static("Disconnected \n"))
