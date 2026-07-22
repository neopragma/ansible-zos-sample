from racf.operations import EnsureTSO
from racf.planner.tso import plan


def test_plan_tso_creates_ensure_tso():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            },
            "tso": {
                "account_number": "ACCT01",
                "procedure": "PROC01",
            },
        }
    }
    result = plan(model)

    assert result == [
        EnsureTSO(
            userid="USER01",
            acct="ACCT01",
            proc="PROC01",
        )
    ]
