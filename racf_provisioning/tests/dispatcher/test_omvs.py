from racf.operations import (
    EnsureUser,
    EnsureOMVS,
)
from racf.dispatcher import dispatch

def test_render_ensure_omvs():
    operation = EnsureOMVS(
        userid="USER01",
        uid=12345,
        home="/u/user01",
        program="/bin/sh",
    )

    assert render(operation) == [
        "ALTUSER USER01 OMVS("
        "UID(12345) "
        "HOME(/u/user01) "
        "PROGRAM(/bin/sh))",
    ]
