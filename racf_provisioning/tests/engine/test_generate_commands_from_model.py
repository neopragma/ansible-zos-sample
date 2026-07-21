from filter_plugins.racf.engine import generate_commands
import pytest

def test_generate_commands_from_model():

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
             },    
        },
    }

    commands = generate_commands(document)

    assert commands == [
        "ADDUSER USER01",
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
        "ALTUSER USER01 TSO(ACCTNUM(ACCT01) PROC(PROC01))",
    ]
