async def exit_command(command_args: list):
    if command_args:
        return "this command doesn't accepts any arguments"

    from dragonion.modules.tui import app

    if app.user_storage.websocket:
        await app.user_storage.websocket.close()
        await app.user_storage.websocket.wait_closed()
    if app.user_storage.sock:
        app.user_storage.sock.close()

    app.exit()
