import os

import click

from ..tui import app


def validate_username(_: click.Context, __: click.Parameter, value: str | None):
    if value is not None and not (4 <= len(value) <= 14):
        raise click.BadParameter("Username length must be from 4 to 14 symbols")
    else:
        return value


@click.command()
@click.option(
    "--auth",
    "-a",
    required=False,
    type=str,
    help="Service name (.auth file with this name should exist in workdir)",
)
@click.option(
    "--username",
    "-u",
    required=False,
    type=str,
    help="Set username",
    callback=validate_username,
)
@click.option(
    "--connect",
    "-c",
    required=False,
    is_flag=True,
    help="Will connect to tor automatically",
)
@click.option(
    "--dev-proxy-port",
    required=False,
    type=int,
    help="Won't start own tor, will try to connect to specified",
)
def cli(
    auth: str | None, username: str | None, connect: bool, dev_proxy_port: int | None
):
    if auth is not None and os.path.isfile(f"{auth}.auth"):
        from ..tui.authentication.utils.results import ServiceAuthResult

        app._pre_service_auth = ServiceAuthResult(f"{auth}.auth")

    if username is not None:
        app._pre_username = username

    app.user_storage.connect = connect
    app.user_storage.dev_proxy_port = dev_proxy_port

    app.run()
