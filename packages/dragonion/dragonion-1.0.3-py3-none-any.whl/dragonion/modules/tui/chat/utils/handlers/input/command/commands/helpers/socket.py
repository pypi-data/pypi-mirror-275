import socks


def connect():
    from dragonion.modules.tui import app

    app.user_storage.sock = socks.socksocket()
    if not app.user_storage.dev_proxy_port:
        app.user_storage.sock.setproxy(
            socks.SOCKS5, *app.user_storage.onion.get_tor_socks_port()
        )
    else:
        app.user_storage.sock.setproxy(
            socks.SOCKS5, "127.0.0.1", app.user_storage.dev_proxy_port
        )

    app.user_storage.sock.connect((app.user_storage.host, 80))
