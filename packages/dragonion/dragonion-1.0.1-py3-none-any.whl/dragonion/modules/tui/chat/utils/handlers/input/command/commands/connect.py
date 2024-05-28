from socks import GeneralProxyError
from textual.widgets import Static

from dragonion.utils.onion import Onion
from dragonion.utils.onion.auth import create_service_auth

from .helpers import socket


async def connect_command(command_args: list):
    if command_args:
        return "this command doesn't accepts any arguments"

    from dragonion.modules.tui import app

    container = app.query_one("MessagesContainer")

    if app.user_storage.onion:
        container.mount(
            Static("Cleaning up existing onion...\n", classes="onion_setup_logs")
        )
        app.user_storage.onion.cleanup()
        app.user_storage.onion = None

    app.user_storage.onion = Onion()
    app.user_storage.host = create_service_auth(
        app.user_storage.onion.tor_data_directory_name,
        service_name=app.service_auth.service_auth_file,
        auth_strings=app.service_auth.raw_auth_strings,
    )

    if not app.user_storage.dev_proxy_port:
        await app.user_storage.onion.connect(
            init_msg_handler=lambda x: container.mount_scroll(
                Static(str(x), classes="onion_setup_logs")
            )
        )

    container.mount_scroll(Static("Connecting socket...", classes="onion_setup_logs"))

    try:
        socket.connect()
    except GeneralProxyError:
        container.write(
            f"Cannot reach service, it may be turned off or you have "
            f"irrelevant id-key pair (auth file)"
        )
        return

    container.mount_scroll(
        Static(
            f"[green]Connected[/] to onion and authenticated "
            f"on {app.user_storage.host}"
        )
    )
    container.query(".onion_setup_logs").remove()
