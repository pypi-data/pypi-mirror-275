from dragonion_core.proto.web.webmessage import WebBroadcastableBuilder


async def handle_message(full_text: str):
    from dragonion.modules.tui import app

    if not app.user_storage.websocket or not app.user_storage.websocket.open:
        app.query_one("MessagesContainer").write(
            f"[red]Error[/]: first connect to onion and join room"
        )
        return

    await app.user_storage.websocket.send(
        WebBroadcastableBuilder(
            avatar=app.user_storage.avatar,
            message_content=full_text,
            from_user=app.identity.username,
            keys=app.user_storage.keys,
        ).to_json()
    )
