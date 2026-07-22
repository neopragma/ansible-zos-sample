"""
Tests for field type validation.
"""

from racf.schema import USER_SCHEMA
from racf.validator import validate

from tests.helpers import (
    assert_invalid,
    assert_has_error,
)


def test_string_accepts_string(valid_user):

    valid_user["content"]["base"]["userid"] = "USER01"

    result = validate(
        valid_user,
        USER_SCHEMA,
        strict=True,
    )

    assert result.valid is True


def test_string_rejects_integer(valid_user):

    valid_user["content"]["base"]["userid"] = 100

    result = validate(
        valid_user,
        USER_SCHEMA,
        strict=True,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "content.base.userid",
    )


def test_integer_rejects_string(valid_user):

    valid_user["content"]["omvs"] = {
        "uid": "1000"
    }

    result = validate(
        valid_user,
        USER_SCHEMA,
        strict=True,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "content.omvs.uid",
    )

def test_section_rejects_non_object_value():

    result = validate(
        {
            "content": "not-an-object"
        },
        USER_SCHEMA,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "content",
    )   
