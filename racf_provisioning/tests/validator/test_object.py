import pytest

from racf.validator import validate
from tests.helpers import assert_valid, assert_invalid, assert_has_error

def test_object_accepts_dictionary(object_schema):
    result = validate(
        {
            "metadata": {
                "owner": "USER01"
            }
        },
        object_schema,
    )

    assert_valid(result)


def test_object_rejects_non_dictionary(object_schema):
    result = validate(
        {
            "metadata": "USER01"
        },
        object_schema,
    )

    assert_invalid(result)
    assert_has_error(result, "metadata")
