from racf.operations import (
    EnsureUser,
    EnsureTSO,
)
from racf.dispatcher import dispatch

def test_render_ensure_tso():
    operation = EnsureTSO(
        userid="USER01",
        acct="ACCT01",
        proc="PROC01",
    )

    assert render(operation) == [
        "ALTUSER USER01 "
        "TSO(ACCTNUM(ACCT01) PROC(PROC01))",
    ]    
