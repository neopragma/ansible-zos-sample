"""
Tests for required field validation.
"""

from filter_plugins.racf.schema import USER_SCHEMA
from filter_plugins.racf.validator import validate

from tests.helpers import (
    assert_valid,
    assert_invalid,
    assert_has_error,
)


def test_required_field_present(valid_user):

    result = validate(
        valid_user,
        USER_SCHEMA,
        strict=True,
    )

    assert_valid(result)


def test_required_field_missing(valid_user):

    del valid_user["content"]["base"]["userid"]

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
