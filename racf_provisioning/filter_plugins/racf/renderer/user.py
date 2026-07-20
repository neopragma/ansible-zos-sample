from ..operations import (
    EnsureOMVS,
    EnsureUser,
)


def render(operation):

    if isinstance(operation, EnsureUser):
        return [
            f"ADDUSER {operation.userid}"
        ]

    if isinstance(operation, EnsureOMVS):
        return [
            (
                f"ALTUSER {operation.userid} "
                f"OMVS("
                f"UID({operation.uid}) "
                f"HOME({operation.home}) "
                f"PROGRAM({operation.program})"
                f")"
            )
        ]

    raise ValueError(
        f"Unsupported operation: {operation}"
    )
