from ..operations import (
    EnsureUser,
    EnsureOMVS,
    EnsureTSO
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

    elif isinstance(operation, EnsureTSO):

        return [
            (
                f"ALTUSER {operation.userid} "
                f"TSO(ACCTNUM({operation.acct}) "
                f"PROC({operation.proc}))"
            )
         ]    

    raise ValueError(
        f"Unsupported operation: {operation}"
    )
