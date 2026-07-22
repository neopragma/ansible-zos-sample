from racf.planner import (
    Plan,
)


def test_plan_starts_empty():

    plan = Plan()

    assert plan.operations == []
