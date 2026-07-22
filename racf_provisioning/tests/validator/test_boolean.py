import pytest

from racf.validator import validate
from tests.helpers import assert_valid, assert_invalid, assert_has_error


def test_boolean_accepts_true(boolean_schema):

    result = validate(
        {
            "enabled": True
        },
        boolean_schema,
    )

    assert_valid(result)


@pytest.mark.parametrize(
    "value",
    [
        "true",
        "false",
        1,
        0,
        [],
        {},
    ],
)
def test_boolean_rejects_non_boolean_values(
    boolean_schema,
    value,
):

    result = validate(
        {
            "enabled": value
        },
        boolean_schema,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "enabled",
    )
