from filter_plugins.racf.planner import plan
from filter_plugins.racf.renderer import render


def test_user_present_pipeline():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            }
        }
    }

    operations = plan(model)

    commands = []

    for operation in operations:
        commands.extend(
            render(operation)
        )

    assert commands == [
        "ADDUSER USER01",
    ]

def test_user_with_omvs_present_pipeline():

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

    operations = plan(model)

    commands = []

    for operation in operations:
        commands.extend(
            render(operation)
        )

    assert commands == [
        "ADDUSER USER01",
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
    ]  



