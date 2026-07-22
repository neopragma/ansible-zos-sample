import pytest

from racf.schema.common import (
    Field,
    Section,
    ValueType,
)


@pytest.fixture
def boolean_schema():
    return Section(
        fields={
            "enabled": Field(
                type=ValueType.BOOLEAN,
                required=True,
            )
        }
    )
