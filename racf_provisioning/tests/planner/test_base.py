from racf.operations import EnsureUser
#from racf.planner.base import plan_base
from racf.planner.base import plan

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
