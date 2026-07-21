from filter_plugins.racf.planner import plan
from filter_plugins.racf.renderer import render
from filter_plugins.racf.validator import validate
from filter_plugins.racf.schema import USER_SCHEMA

def test_user_present_pipeline():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            }
        }
    }
    
    commands = []

    plan_result = plan(model)
    for operation in plan_result.operations:
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
    
    commands = []
    plan_result = plan(model)
    for operation in plan_result.operations:
        commands.extend(
            render(operation)
        )
    assert commands == [
        "ADDUSER USER01",
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
    ]  

def test_user_profile_end_to_end():

    document = {
        "state": "present",
        "meta": {
            "object_type": "user",
            "schema_version": "0.1.0",
            "zos_version": "3.1.0",
        },
        "content": {
            "base": {
                "userid": "USER01",
            },
            "omvs": {
                "uid": 12345,
                "home": "/u/user01",
                "program": "/bin/sh",
            },
            "tso": {
            "acct": "ACCT01",
            "proc": "PROC01",
            }
        },
    }

    result = validate(
        document,
        USER_SCHEMA,
    )

    assert result.valid is True
    operations = plan(document)
    commands = []
    plan_result = plan(document)
    for operation in plan_result.operations:
        commands.extend(
            render(operation)
        )
    assert commands == [
        "ADDUSER USER01",
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
        "ALTUSER USER01 TSO(ACCTNUM(ACCT01) PROC(PROC01))",
    ]    

