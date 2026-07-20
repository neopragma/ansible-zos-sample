from filter_plugins.racf.operations import (
    EnsureOMVS,
    EnsureUser,
)

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

    result = plan(model)
    assert len(result.operations) == 1
    assert isinstance(
        result.operations[0],
        EnsureUser,
    )
    assert result.operations == [
        EnsureUser(
            userid="USER01",
        ),
    ]

def test_plan_user_with_omvs_creates_ensure_omvs():
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

    result = plan(model)
    assert len(result.operations) == 2
    assert isinstance(
        result.operations[0],
        EnsureUser,
    )
    assert EnsureOMVS(
        userid="USER01",
        uid=12345,
        home="/u/user01",
        program="/bin/sh",
    ) in result.operations    

def test_plan_user_without_omvs_does_not_create_ensure_omvs():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            },
        }
    }

    result = plan(model)
    assert len(result.operations) == 1
    assert isinstance(
        result.operations[0],
        EnsureUser,
    )
    assert EnsureUser(
        userid="USER01",
    ) in result.operations

    assert not any(
        isinstance(operation, EnsureOMVS)
        for operation in result.operations
    )

def test_plan_user_creates_operations_in_dependency_order():

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

    result = plan(model)
    assert len(result.operations) == 2
    assert isinstance(
        result.operations[0],
        EnsureUser,
    )
    assert isinstance(
        result.operations[0],
        EnsureUser,
    )

    assert isinstance(
        result.operations[1],
        EnsureOMVS,
    )
    
