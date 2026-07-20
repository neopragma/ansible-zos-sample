from filter_plugins.racf.planner import (
    Plan,
    plan,
)

# This is to guard against inadvertently removing imports when making changes.
def test_planner_public_api():

    assert callable(plan)
    assert Plan is not None
