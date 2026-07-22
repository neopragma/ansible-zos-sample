from racf.operations import EnsureTSO
from racf.dispatcher import dispatch
from racf.strategy import SeparateCommandsStrategy


def test_dispatch_ensure_tso():

    operation = EnsureTSO(
        userid="USER01",    
        account_number="ACCT001",
        procedure="PROC01",
    )

    commands = dispatch(
        [operation],
        SeparateCommandsStrategy(),
    )

    assert commands == [
        "ALTUSER USER01 TSO("
        "ACCTNUM(ACCT001) "
        "PROC(PROC01))",
    ]
