from racf.operations import (
    EnsureOMVS,
    EnsureUser,
)
from racf.planner import plan


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

    result = plan(model)
    operations = result.operations
    
    assert operations == [
        EnsureUser(userid="USER01"),
        EnsureOMVS(
            userid="USER01",
            uid=12345,
            home="/u/user01",
            program="/bin/sh",
        ),
    ]
