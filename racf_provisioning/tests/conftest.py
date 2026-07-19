"""
Shared pytest fixtures.
"""

import pytest


@pytest.fixture
def valid_user():
    """
    Return the smallest valid RACF user model.

    This fixture intentionally contains only the minimum
    required fields needed for validator tests.
    """

    return {
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
        },
    }
