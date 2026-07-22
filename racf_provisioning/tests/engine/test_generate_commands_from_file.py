from racf.engine import generate_commands
from racf.engine import generate_commands_from_file
import pytest

def test_generate_commands_from_file(tmp_path):
    filename = tmp_path / "USER01.yml"
    filename.write_text("""
racf_user:
  meta:
    object_type: user
    schema_version: "0.1.0"
    zos_version: "3.1.0"

  state: present

  content:
    base:
      userid: USER01

    omvs:
      uid: 12345
      home: /u/user01
      program: /bin/sh

    tso:
      account_number: ACCT01
      procedure: PROC01    
""")

    commands = generate_commands_from_file(str(filename))

    assert commands == [
        "ADDUSER USER01",
        "ALTUSER USER01 OMVS(UID(12345) HOME(/u/user01) PROGRAM(/bin/sh))",
        "ALTUSER USER01 TSO(ACCTNUM(ACCT01) PROC(PROC01))",        
    ]

def test_rejects_missing_userid(tmp_path):
    filename = tmp_path / "USER01.yml"
    filename.write_text("""
racf_user:
  meta:
    object_type: user
    schema_version: "0.1.0"
    zos_version: "3.1.0"

  state: present

  content:
    base:

    omvs:
      uid: 12345
      home: /u/user01
      program: /bin/sh

    tso:
      account_number: ACCT01
      procedure: PROC01    
""")

    with pytest.raises(ValueError) as excinfo:
        generate_commands(str(filename))

    assert "must be an object" in str(excinfo.value)
