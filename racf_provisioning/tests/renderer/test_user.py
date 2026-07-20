from filter_plugins.racf.operations import EnsureUser
from filter_plugins.racf.renderer import render


def test_render_ensure_user():

    operation = EnsureUser(
        userid="USER01",
    )

    commands = render(operation)

    assert commands == [
        "ADDUSER USER01",
    ]
