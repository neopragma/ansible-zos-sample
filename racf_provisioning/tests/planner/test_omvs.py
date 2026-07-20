from filter_plugins.racf.operations import (
    EnsureOMVS,
    EnsureUser,
)
from filter_plugins.racf.planner import plan


def test_plan_user_with_omvs():

    model = {
        "state": "present",
        "content": {
            "base": {
                "userid": "USER01",
            },
            "omvs": {
                "uid": 12345,
                "home": "/u/user01",
                "program": "/bin/sh",
            },
        },
    }

    operations = plan(model)

    assert operations == [
        EnsureUser(userid="USER01"),
        EnsureOMVS(
            userid="USER01",
            uid=12345,
            home="/u/user01",
            program="/bin/sh",
        ),
    ]
