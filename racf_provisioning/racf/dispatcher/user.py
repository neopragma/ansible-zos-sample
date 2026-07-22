from racf.operations.user import EnsureUser
from racf.operations.omvs import EnsureOMVS
from racf.operations.tso import EnsureTSO


def dispatch_user(op: EnsureUser, strategy):
    strategy.adduser(op.userid)


def dispatch_omvs(op: EnsureOMVS, strategy):

    body = []

    body.append(f"UID({op.uid})")
    body.append(f"HOME({op.home})")
    body.append(f"PROGRAM({op.program})")

    strategy.segment(
        op.userid,
        "OMVS",
        body,
    )


def dispatch_tso(op: EnsureTSO, strategy):

    body = []

    if op.account_number:
        body.append(f"ACCTNUM({op.account_number})")

    if op.procedure:
        body.append(f"PROC({op.procedure})")

    strategy.segment(
        op.userid,
        "TSO",
        body,
    )
