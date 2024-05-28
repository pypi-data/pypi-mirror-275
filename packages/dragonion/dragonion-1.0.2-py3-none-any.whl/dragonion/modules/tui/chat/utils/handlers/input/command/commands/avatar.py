from dragonion.utils.core.emoji import random_emoji


async def avatar_command(command_args: list):
    from dragonion.modules.tui import app

    container = app.query_one("MessagesContainer")
    if not command_args:
        app.user_storage.avatar = random_emoji()
        container.write(f"Random emoji set: {app.user_storage.avatar}")
        return

    if len(command_args[0]) != 1:
        return "avatar length must be exactly 1 symbol"
    else:
        app.user_storage.avatar = command_args[0]
        container.write(f"Avatar set to: {app.user_storage.avatar}")
