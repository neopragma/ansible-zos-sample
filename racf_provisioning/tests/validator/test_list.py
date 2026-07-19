import pytest

from filter_plugins.racf.validator import validate
from tests.helpers import assert_valid, assert_invalid, assert_has_error

def test_list_accepts_list(list_schema):
    result = validate(
        {"groups": ["SYS1", "SYS2"]},
        list_schema,
    )

    assert_valid(result)


def test_list_rejects_non_list(list_schema):
    result = validate(
        {"groups": "SYS1"},
        list_schema,
    )

    assert_invalid(result)
    assert_has_error(result, "groups")
