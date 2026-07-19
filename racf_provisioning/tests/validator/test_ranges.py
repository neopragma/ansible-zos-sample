"""
Tests for numeric range validation.
"""
import pytest

from filter_plugins.racf.schema.common import (
    Field,
    Section,
    ValueType,
)

from filter_plugins.racf.validator import validate

from tests.helpers import (
    assert_valid,
    assert_invalid,
    assert_has_error,
)


from filter_plugins.racf.schema.common import (
    Field,
    Section,
    ValueType,
)

from filter_plugins.racf.validator import validate

from tests.helpers import (
    assert_valid,
    assert_invalid,
    assert_has_error,
)


@pytest.fixture
def integer_range_schema():
    return Section(
        fields={
            "value": Field(
                type=ValueType.INTEGER,
                required=True,
                minimum=1,
                maximum=10,
            )
        },
        sections={},
    )


def test_integer_equal_to_minimum(integer_range_schema):

    result = validate(
        {"value": 1},
        integer_range_schema,
    )

    assert_valid(result)


def test_integer_equal_to_maximum(integer_range_schema):

    result = validate(
        {"value": 10},
        integer_range_schema,
    )

    assert_valid(result)


def test_integer_below_minimum(integer_range_schema):

    result = validate(
        {"value": 0},
        integer_range_schema,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "value",
    )


def test_integer_above_maximum(integer_range_schema):

    result = validate(
        {"value": 11},
        integer_range_schema,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "value",
    )

def test_integer_rejects_string_with_range_schema(integer_range_schema):

    result = validate(
        {"value": "5"},
        integer_range_schema,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "value",
    )

def test_integer_below_minimum_returns_single_error(
    integer_range_schema,
):

    result = validate(
        {"value": 0},
        integer_range_schema,
    )

    assert_invalid(result)

    assert len(result.errors) == 1

    assert_has_error(
        result,
        "value",
    )    
