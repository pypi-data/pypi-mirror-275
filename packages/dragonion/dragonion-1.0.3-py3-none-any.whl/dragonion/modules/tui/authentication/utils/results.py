from dataclasses import dataclass
from typing import Optional


@dataclass
class ServiceAuthResult:
    service_auth_file: Optional[str] = None
    raw_auth_strings: Optional[tuple[str, str]] = None

    def __post_init__(self):
        """
        Validate service auth result, one of parameters must be valid and other must be
        None
        :return:
        """
        self.raw_auth_strings = (
            None if self.raw_auth_strings == ("", "") else self.raw_auth_strings
        )
        _is_auth_string = (
            self.raw_auth_strings is not None and not self.raw_auth_strings == ("", "")
        )

        if self.service_auth_file is None and not _is_auth_string:
            raise ValueError("Exactly one argument should have a value")
        elif self.service_auth_file is not None and _is_auth_string:
            raise ValueError("Only one argument should have a value")

        if self.service_auth_file and not self.service_auth_file.endswith(".auth"):
            raise ValueError("Service auth file should end with .auth")

        # noinspection PyUnresolvedReferences
        if _is_auth_string and (
            len(self.raw_auth_strings[0]) != 56
            or not all(c.isdigit() or c.islower() for c in self.raw_auth_strings[0])
        ):
            raise ValueError("Incorrect service id")

        # noinspection PyUnresolvedReferences
        if _is_auth_string and (
            len(self.raw_auth_strings[1]) != 52
            or not all(c.isdigit() or c.isupper() for c in self.raw_auth_strings[1])
        ):
            raise ValueError("Incorrect auth string")
