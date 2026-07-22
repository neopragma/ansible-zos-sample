"""
Tests for validator strict mode.
"""

from racf.schema import USER_SCHEMA
from racf.validator import validate

from tests.helpers import (
    assert_valid,
    assert_invalid,
    assert_has_error,
)

def test_strict_rejects_unknown_field():

    data = {
        "state": "present",
        "meta": {
            "object_type": "user",
            "schema_version": "0.1.0",
            "zos_version": "3.1.0",
        },
        "content": {
            "base": {
                "userid": "USER01",
                "favorite_color": "blue",
            }
        },
    }

    result = validate(
        data,
        USER_SCHEMA,
        strict=True,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "content.base.favorite_color",
    )

def test_non_strict_accepts_unknown_field():

    data = {
        "state": "present",
        "meta": {
            "object_type": "user",
            "schema_version": "0.1.0",
            "zos_version": "3.1.0",
        },
        "content": {
            "base": {
                "userid": "USER01",
                "favorite_color": "blue",
            }
        },
    }

    result = validate(
        data,
        USER_SCHEMA,
        strict=False,
    )

    assert_valid(result)
    assert result.errors == []


def test_strict_rejects_unknown_section():

    data = {
        "state": "present",
        "meta": {
            "object_type": "user",
            "schema_version": "0.1.0",
            "zos_version": "3.1.0",
        },
        "content": {
            "base": {
                "userid": "USER01",
            },
            "pizza": {
                "pepperoni": True,
            },
        },
    }

    result = validate(
        data,
        USER_SCHEMA,
        strict=True,
    )

    assert_invalid(result)

    assert_has_error(
        result,
        "content.pizza",
    )

def test_non_strict_accepts_unknown_section():
      
    data = {
        "state": "present",
        "meta": {
            "object_type": "user",
            "schema_version": "0.1.0",
            "zos_version": "3.1.0",
        },
        "content": {
            "base": {
                "userid": "USER01",
            },
            "pizza": {
                "pepperoni": True,
            },
        },
    }

    result = validate(
        data,
        USER_SCHEMA,
        strict=False,
    )

    assert_valid(result)
    assert result.errors == []

def test_boolean_rejects_string(boolean_schema):
    result = validate(
        {"enabled": "true"},
        boolean_schema,
    )

    assert_invalid(result)
    assert_has_error(result, "enabled")

def test_boolean_accepts_true(boolean_schema):
    result = validate(
        {"enabled": True},
        boolean_schema,
    )

    assert_valid(result)
    

