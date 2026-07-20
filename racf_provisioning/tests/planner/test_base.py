from filter_plugins.racf.operations import EnsureUser
#from filter_plugins.racf.planner.base import plan_base
from filter_plugins.racf.planner.base import plan

def test_plan_base():

    model = {
        "content": {
            "base": {
                "userid": "USER01",
            },
        }
    }
    assert plan(model) == [
        EnsureUser(
            userid="USER01",
        ),
    ]
