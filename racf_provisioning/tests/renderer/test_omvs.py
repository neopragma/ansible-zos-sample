from filter_plugins.racf.operations import EnsureOMVS
from filter_plugins.racf.renderer import render


def test_render_ensure_omvs():

    operation = EnsureOMVS(
        userid="USER01",
        uid=12345,
        home="/u/user01",
        program="/bin/sh",
    )

    commands = render(operation)

    assert commands == [
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
    ]
