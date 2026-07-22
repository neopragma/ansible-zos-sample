from racf.operations import EnsureOMVS
from racf.dispatcher import dispatch
from racf.strategy import SeparateCommandsStrategy


def test_dispatch_ensure_omvs():

    operation = EnsureOMVS(
        userid="USER01",
        uid=12345,
        home="/u/user01",
        program="/bin/sh",
    )

    commands = dispatch(
        [operation],
        SeparateCommandsStrategy(),
    )

    assert commands == [
        "ALTUSER USER01 OMVS("
        "UID(12345) "
        "HOME(/u/user01) "
        "PROGRAM(/bin/sh))",
    ]
