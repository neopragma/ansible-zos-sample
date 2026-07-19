"""
Common domain model classes used by RACF provisioning.

The model layer represents desired RACF state.
It intentionally contains no RACF command syntax and no Ansible-specific logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RacfObject:
    """
    Base class for all RACF domain objects.

    Examples:
        RacfUser
        RacfGroup
        RacfDataset

    Attributes:
        state:
            Desired lifecycle state.

            Expected values:
                present
                absent

        meta:
            Metadata associated with the object definition.

        content:
            Object-specific desired state.
    """

    state: str

    meta: dict[str, Any] = field(default_factory=dict)

    content: dict[str, Any] = field(default_factory=dict)


@dataclass
class Operation:
    """
    Represents a logical operation against a RACF object.

    This is intentionally not a RACF command.

    Example:

        Operation(
            action="remove_connection",
            object_type="group",
            object_name="OPERATIONS"
        )

    may eventually render into:

        CONNECT userid GROUP(OPERATIONS) REMOVE

    or another sequence of commands.

    The planner creates Operations.
    The renderer converts Operations into RACF commands.
    """

    action: str

    object_type: str

    object_name: str

    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class Command:
    """
    Represents a RACF command before text rendering.

    Renderers create Commands.

    Example:

        Command(
            verb="ALTUSER",
            operands=[
                "IBMUSER",
                "NOOPERATIONS"
            ]
        )

    Later converted to:

        ALTUSER IBMUSER NOOPERATIONS

    Keeping this structured avoids string parsing throughout the framework.
    """

    verb: str

    operands: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        """
        Render the command as a single line.

        This is only presentation.
        Logic should operate on Command objects.
        """

        if self.operands:
            return f"{self.verb} {' '.join(self.operands)}"

        return self.verb
