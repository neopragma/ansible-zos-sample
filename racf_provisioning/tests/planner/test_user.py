from filter_plugins.racf.operations import EnsureUser
from filter_plugins.racf.planner import plan


def test_plan_minimal_user():

    model = {
        "state": "present",
        "content": {
            "base": {
                "userid": "USER01",
            },
        },
    }

    operations = plan(model)

    assert operations == [
        EnsureUser(
            userid="USER01",
        ),
    ]
