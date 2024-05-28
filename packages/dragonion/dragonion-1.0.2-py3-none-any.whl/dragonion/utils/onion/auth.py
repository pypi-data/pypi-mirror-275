import os

from dragonion_core.proto.file import AuthFile


def create_service_auth(
    tor_data_directory_name: str,
    service_name: str = None,
    auth_strings: tuple[str, str] = None,
) -> str:
    """
    Creates .auth_private file to endpoint be accessible
    :param tor_data_directory_name: Current temp directory of tor
    :param service_name: Name of .auth file user got from server hoster
    :param auth_strings: service_id, key
    :return: Returns .onion url of service
    """
    if service_name:
        auth = AuthFile(service_name)
        with open(
            os.path.join(
                os.path.join(tor_data_directory_name, "auth"), "service.auth_private"
            ),
            "w",
        ) as f:
            f.write(auth["auth"])

        return auth["host"]
    elif auth_strings[0] and auth_strings[1]:
        with open(
            os.path.join(
                os.path.join(tor_data_directory_name, "auth"), "service.auth_private"
            ),
            "w",
        ) as f:
            f.write(f"{auth_strings[0]}:descriptor:" f"x25519:{auth_strings[1]}")

        return f"{auth_strings[0]}.onion"
