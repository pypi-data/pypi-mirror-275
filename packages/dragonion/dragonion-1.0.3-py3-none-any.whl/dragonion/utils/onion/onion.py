import os
import platform
import random
import socket
import tempfile
import time
from asyncio import subprocess

import psutil
from rich import print
from stem.control import Controller

from dragonion.utils.core import dirs

from .stem_process import launch_tor_with_config


def get_available_port(min_port, max_port):
    with socket.socket() as tmpsock:
        while True:
            try:
                tmpsock.bind(("127.0.0.1", random.randint(min_port, max_port)))
                break
            except OSError:
                pass
        _, port = tmpsock.getsockname()
    return port


class Onion(object):
    c: Controller
    tor_control_socket: str | None
    tor_control_port: int | None
    tor_torrc: str
    tor_socks_port: int
    tor_cookie_auth_file: str
    tor_path: str = dirs.get_tor_paths()
    tor_proc: subprocess.Process | None
    connected_to_tor: bool = False
    auth_string: str
    graceful_close_onions: list = list()

    def __init__(self):
        self.tor_data_directory = tempfile.TemporaryDirectory(dir=dirs.build_tmp_dir())
        self.tor_data_directory_name = self.tor_data_directory.name
        os.makedirs(os.path.join(self.tor_data_directory_name, "auth"))

    def kill_same_tor(self):
        """
        Kills tor process that looks like process to be created now
        """
        for proc in psutil.process_iter(["pid", "name", "username"]):
            try:
                cmdline = proc.cmdline()
                if (
                    cmdline[0] == self.tor_path
                    and cmdline[1] == "-f"
                    and cmdline[2] == self.tor_torrc
                ):
                    proc.terminate()
                    proc.wait()
                    break
            except Exception as e:
                assert e

    def get_config(self, tor_data_directory_name: str) -> dict:
        """
        Build config dict for launching tor
        :param tor_data_directory_name: Data directory for tor, can be generated
                                        using code from core/dirs
        :return:
        """
        self.tor_cookie_auth_file = os.path.join(tor_data_directory_name, "cookie")
        try:
            self.tor_socks_port = get_available_port(1000, 65535)
        except Exception as e:
            print(f"Cannot bind any port for socks proxy: {e}")
        self.tor_torrc = os.path.join(tor_data_directory_name, "torrc")

        self.kill_same_tor()

        config = {
            "DataDirectory": tor_data_directory_name,
            "SocksPort": str(self.tor_socks_port),
            "CookieAuthentication": "1",
            "CookieAuthFile": self.tor_cookie_auth_file,
            "ClientOnionAuthDir": os.path.join(tor_data_directory_name, "auth"),
            "AvoidDiskWrites": "1",
            "Log": ["NOTICE stdout"],
        }

        if (
            platform.system() in ["Windows", "Darwin"]
            or len(tor_data_directory_name) > 90
        ):
            try:
                self.tor_control_port = get_available_port(1000, 65535)
                config = config | {"ControlPort": str(self.tor_control_port)}
            except Exception as e:
                print(f"Cannot bind any control port: {e}")
            self.tor_control_socket = None
        else:
            self.tor_control_port = None
            self.tor_control_socket = os.path.abspath(
                os.path.join(tor_data_directory_name, "control_socket")
            )
            config = config | {"ControlSocket": str(self.tor_control_socket)}

        return config

    async def connect(self, init_msg_handler=print):
        """
        Connect to tor network
        :param init_msg_handler: Function that will print logs
        :return:
        """
        self.tor_proc = await launch_tor_with_config(
            config=self.get_config(self.tor_data_directory_name),
            tor_cmd=self.tor_path,
            take_ownership=True,
            init_msg_handler=init_msg_handler,
        )

        time.sleep(2)

        if not self.tor_control_socket:
            self.c = Controller.from_port(port=self.tor_control_port)
            self.c.authenticate()
        else:
            self.c = Controller.from_socket_file(path=self.tor_control_socket)
            self.c.authenticate()

        self.connected_to_tor = True

    def is_authenticated(self):
        """
        Check if controller authenticated
        :return:
        """
        if self.c is not None:
            return self.c.is_authenticated()
        else:
            return False

    def cleanup(self):
        """
        Stop tor and clean up (hopefully) all footprints
        :return:
        """
        if self.tor_proc:
            try:
                rendezvous_circuit_ids = []
                for c in self.c.get_circuits():
                    if (
                        c.purpose == "HS_SERVICE_REND"
                        and c.rend_query in self.graceful_close_onions
                    ):
                        rendezvous_circuit_ids.append(c.id)

                symbols = list("\\|/-")
                symbols_i = 0

                while True:
                    num_rend_circuits = 0
                    for c in self.c.get_circuits():
                        if c.id in rendezvous_circuit_ids:
                            num_rend_circuits += 1

                    if num_rend_circuits == 0:
                        print("\rTor rendezvous circuits have closed" + " " * 20)
                        break

                    if num_rend_circuits == 1:
                        circuits = "circuit"
                    else:
                        circuits = "circuits"
                    print(
                        f"\rWaiting for {num_rend_circuits} Tor rendezvous {circuits} "
                        f"to close {symbols[symbols_i]} ",
                        end="",
                    )
                    symbols_i = (symbols_i + 1) % len(symbols)
                    time.sleep(1)
            except Exception as e:
                print(e)

            try:
                self.tor_proc.terminate()
                time.sleep(0.2)
            except Exception as e:
                assert e
            try:
                self.tor_proc.kill()
                time.sleep(0.2)
            except Exception as e:
                assert e
            self.tor_proc = None

        self.connected_to_tor = False

        try:
            self.tor_data_directory.cleanup()
        except Exception as e:
            print(f"Cannot cleanup temporary directory: {e}")

    def get_tor_socks_port(self):
        return "127.0.0.1", self.tor_socks_port
