from filter_plugins.racf.operations import EnsureOMVS
from filter_plugins.racf.planner.omvs import plan


def test_plan_omvs():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            },
            "omvs": {
                "uid": 12345,
                "home": "/u/user01",
                "program": "/bin/sh",
            },
        }
    }

    assert plan(model) == [
        EnsureOMVS(
            userid="USER01",
            uid=12345,
            home="/u/user01",
            program="/bin/sh",
        ),
    ]

def test_plan_without_omvs():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            },
        }
    }

    assert plan(model) == []    
