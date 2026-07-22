from racf.operations.user import EnsureUser
from racf.operations.omvs import EnsureOMVS
from racf.operations.tso import EnsureTSO

from .user import (
    dispatch_user,
    dispatch_omvs,
    dispatch_tso,
)


def dispatch(operations, strategy):

    for op in operations:

        if isinstance(op, EnsureUser):
            dispatch_user(op, strategy)

        elif isinstance(op, EnsureOMVS):
            dispatch_omvs(op, strategy)

        elif isinstance(op, EnsureTSO):
            dispatch_tso(op, strategy)

    return strategy.commands()
