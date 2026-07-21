from filter_plugins.racf.operations import EnsureTSO
from filter_plugins.racf.planner.tso import plan


def test_plan_tso_creates_ensure_tso():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            },
            "tso": {
                "acct": "ACCT01",
                "proc": "PROC01",
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
