"""
Test assertion helpers.
"""


def assert_valid(result):
    """
    Assert that validation succeeded.
    """

    assert result.valid is True
    assert result.errors == []


def assert_invalid(result):
    """
    Assert that validation failed.
    """

    assert result.valid is False
    assert len(result.errors) > 0


def assert_has_error(result, path):
    """
    Assert that a validation error exists for a path.
    """

    assert path in [
        error.path
        for error in result.errors
    ]
