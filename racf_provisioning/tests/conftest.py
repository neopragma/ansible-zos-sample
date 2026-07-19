"""
Shared pytest fixtures.
"""

import pytest
import pytest

from filter_plugins.racf.schema.common import (
    Field,
    Section,
    ValueType,
)

@pytest.fixture
def list_schema():
    return Section(
        fields={
            "groups": Field(
                type=ValueType.LIST,
                required=True,
            )
        }
    )

@pytest.fixture
def object_schema():
    return Section(
        fields={
            "metadata": Field(
                type=ValueType.OBJECT,
                required=True,
            )
        }
    )

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




@pytest.fixture
def list_schema():
    return Section(
        fields={
            "groups": Field(
                type=ValueType.LIST,
                required=True,
            )
        }
    )


@pytest.fixture
def object_schema():
    return Section(
        fields={
            "metadata": Field(
                type=ValueType.OBJECT,
                required=True,
            )
        }
    )    
