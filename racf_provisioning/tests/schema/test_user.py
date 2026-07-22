"""
Tests for RACF schemas.
"""

from racf.schema import (
    USER_SCHEMA,
    ValueType,
)


def test_user_schema_contains_expected_sections():

    assert "meta" in USER_SCHEMA.sections

    assert "content" in USER_SCHEMA.sections


def test_user_schema_contains_base_segments():

    content = USER_SCHEMA.sections["content"]


    assert "base" in content.sections

    assert "omvs" in content.sections

    assert "tso" in content.sections


def test_userid_is_required_string():

    base = (
        USER_SCHEMA
        .sections["content"]
        .sections["base"]
    )


    userid = base.fields["userid"]


    assert userid.required is True

    assert userid.type == ValueType.STRING
