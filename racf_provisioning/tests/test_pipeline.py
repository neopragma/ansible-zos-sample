from racf.engine import generate_commands
from racf.validator import validate
from racf.schema import USER_SCHEMA


def test_user_present_pipeline():

    model = {
        "state": "present",
        "meta": {
            "object_type": "user",
            "schema_version": "0.1.0",
            "zos_version": "3.1.0",
        },
        "content": {
            "base": {
                "userid": "USER01",
            }
        },
    }

    commands = generate_commands(model)

    assert commands == [
        "ADDUSER USER01",
    ]


def test_user_with_omvs_present_pipeline():

    model = {
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
        },
    }

    commands = generate_commands(model)

    assert commands == [
        "ADDUSER USER01",
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
    ]


def test_user_profile_end_to_end():

    model = {
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
                "account_number": "ACCT01",
                "procedure": "PROC01",
            },
        },
    }

    commands = generate_commands(model)

    assert commands == [
        "ADDUSER USER01",
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
        "ALTUSER USER01 TSO(ACCTNUM(ACCT01) PROC(PROC01))",
    ]
