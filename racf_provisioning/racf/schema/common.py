"""
Common schema primitives used by RACF object schemas.

The schema layer describes:

    - structure
    - data types
    - validation constraints

It intentionally does not contain:

    - RACF command generation logic
    - Ansible logic
    - object-specific rules
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ValueType(Enum):
    """
    Supported schema value types.
    """

    STRING = "string"

    INTEGER = "integer"

    BOOLEAN = "boolean"

    ENUM = "enum"

    LIST = "list"

    OBJECT = "object"


@dataclass(frozen=True)
class Field:
    """
    Metadata describing one schema field.

    A Field answers questions such as:

        - Is this field required?
        - What type should it contain?
        - What values are allowed?
        - What validation constraints apply?

    Example:

        Field(
            type=ValueType.INTEGER,
            minimum=1
        )

    describes an integer value that must be greater than or equal to one.
    """

    type: ValueType

    required: bool = False

    choices: tuple[str, ...] | None = None

    minimum: int | None = None

    maximum: int | None = None

    default: Any = None

    description: str = ""


@dataclass(frozen=True)
class Section:
    """
    A hierarchical schema section.

    A Section contains:

        fields:
            Leaf values.

        sections:
            Nested objects.

    Example:

        content:
            base:
                userid

    becomes:

        Section(
            sections={
                "base": Section(
                    fields={
                        "userid": Field(...)
                    }
                )
            }
        )
    """

    fields: dict[str, Field] = field(default_factory=dict)

    sections: dict[str, "Section"] = field(default_factory=dict)


def field_path_join(*parts: str) -> str:
    """
    Build a dotted schema path.

    Example:

        field_path_join(
            "content",
            "base",
            "userid"
        )

        returns:

        "content.base.userid"

    This will be useful for validation messages.
    """

    return ".".join(parts)
