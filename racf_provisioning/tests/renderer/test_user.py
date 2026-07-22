from racf.operations import (
    EnsureUser,
)
from racf.renderer import render

def test_render_ensure_user():
    operation = EnsureUser(userid="USER01")

    assert render(operation) == [
        "ADDUSER USER01",
    ]   
