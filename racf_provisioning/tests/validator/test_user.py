"""
Tests for the generic schema validator.
"""

import pytest
from filter_plugins.racf.exceptions import (
    SchemaValidationError,
)
from filter_plugins.racf.schema import USER_SCHEMA
from filter_plugins.racf.validator import validate

def test_valid_user_profile():
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
            }
        }
    }

    validate(
        data,
        USER_SCHEMA,
        True,
    )

def test_missing_required_userid():
    data = {
        "state": "present",
        "meta": {
            "object_type": "user",
            "schema_version": "0.1.0",
            "zos_version": "3.1.0",
        },
        "content": {
            "base": {}
        }
    }

    result = validate(
        data,
        USER_SCHEMA,
        True,
    )

    assert result.valid is False

    assert (
        "content.base.userid"
        in [
            error.path
            for error in result.errors
        ]
    )


def test_invalid_state():
    data = {
        "state": "create",
    }

    result = validate(
        data,
        USER_SCHEMA,
        True,
    )

    assert result.valid is False

    assert (
        "state"
        in [
            error.path
            for error in result.errors
        ]
    )

def test_invalid_uid_type():
    data = {
        "state": "present",
        "content": {
            "omvs": {
                "uid": "1000",
            }
        }
    }

    result = validate(
        data,
        USER_SCHEMA,
        True
    )

    assert result.valid is False

    assert (
        "content.omvs.uid"
        in [
            error.path
            for error in result.errors
        ]
    )
