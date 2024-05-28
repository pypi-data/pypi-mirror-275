import os
import platform
import shutil
import sys

from . import const


def get_resource_path(filename):
    """
    Get path to file in resources folder
    :param filename: Resource name to get path
    :return:
    """
    if const.portable:
        # noinspection PyUnresolvedReferences, PyProtectedMember
        application_path = os.path.join(os.path.abspath(sys._MEIPASS), "resources")
    else:
        import dragonion

        application_path = os.path.join(
            os.path.dirname(dragonion.__file__), "resources"
        )

    return os.path.join(application_path, filename)


def get_tor_paths():
    """
    Get path to tor executable and download it if not exists. Will exit application on
    ARM systems if tor is not installed.
    :return: Path to tor executable
    """
    if platform.system() != "Darwin" and platform.machine().lower() in [
        "aarch64",
        "arm64",
    ]:
        if shutil.which("tor"):
            return "tor"
        else:
            print(
                "Detected ARM system and tor is not installed or added to PATH. "
                "Please, consider reading documentation and installing application "
                "properly"
            )
            sys.exit(1)

    else:
        from ..onion.tor_downloader import download_tor

        if platform.system() in ["Linux", "Darwin"]:
            tor_path = os.path.join(build_data_dir(), "tor/tor")
        elif platform.system() == "Windows":
            tor_path = os.path.join(build_data_dir(), "tor/tor.exe")
        else:
            raise Exception("Platform not supported")

        if not os.path.isfile(tor_path):
            download_tor(dist=build_data_dir())

        return tor_path


def build_data_dir():
    """
    Get local data dir
    :return:
    """
    if const.portable:
        # noinspection PyUnresolvedReferences, PyProtectedMember
        dragonion_data_dir = os.path.join(os.path.abspath(sys._MEIPASS), "data")
    else:
        import dragonion

        dragonion_data_dir = os.path.join(os.path.dirname(dragonion.__file__), "data")

    os.makedirs(dragonion_data_dir, exist_ok=True)
    return dragonion_data_dir


def build_tmp_dir():
    """
    Get "tmp" dir in data directory
    :return:
    """
    tmp_dir = os.path.join(build_data_dir(), "tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    return tmp_dir


def build_persistent_dir():
    """
    Get "persistent" dir in data directory
    :return:
    """
    persistent_dir = os.path.join(build_data_dir(), "persistent")
    os.makedirs(persistent_dir, exist_ok=True)
    return persistent_dir


def build_tor_data_dir():
    """
    Get "tor_data" dir in data directory
    :return:
    """
    tor_dir = os.path.join(build_data_dir(), "tor_data")
    os.makedirs(tor_dir, exist_ok=True)
    return tor_dir
