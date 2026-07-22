from racf.operations import (
    EnsureUser,
)
from racf.dispatcher import dispatch
from racf.strategy import SeparateCommandsStrategy

def test_dispatch_ensure_user():
    operation = EnsureUser(userid="USER01")

    assert dispatch(
        [ operation ], SeparateCommandsStrategy())  == [
        "ADDUSER USER01",
    ]   
