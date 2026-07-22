"""
Tests for enum validation.
"""

import pytest

from racf.schema.common import (
    Field,
    Section,
    ValueType,
)

from racf.validator import validate

from tests.helpers import (
    assert_valid,
    assert_invalid,
    assert_has_error,
)


@pytest.fixture
def enum_schema():

    return Section(
        fields={
            "authority": Field(
                type=ValueType.ENUM,
                required=True,
                choices=[
                    "use",
                    "connect",
                    "join",
                    "create",
                ],
            )
        },
        sections={},
    )


def test_enum_accepts_valid_value(enum_schema):

    result = validate(
        {
            "authority": "connect"
        },
        enum_schema,
    )

    assert_valid(result)


def test_enum_rejects_invalid_value(enum_schema):

    result = validate(
        {
            "authority": "invalid"
        },
        enum_schema,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "authority",
    )


@pytest.mark.parametrize(
    "value",
    [
        123,
        [],
        {},
        True
    ],
)
def test_enum_rejects_non_matching_types(
    enum_schema,
    value,
):
    print(enum_schema.fields["authority"])
    print(enum_schema.fields["authority"].type)
    print(enum_schema.fields["authority"].choices)
    result = validate(
        {
            "authority": value
        },
        enum_schema,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "authority",
    )

def test_enum_rejects_integer(enum_schema):

    result = validate(
        {
            "authority": 123,
        },
        enum_schema,
    )

    print(result)

    assert_invalid(result)    
