"""
RACF user domain model.

This module defines the in-memory representation of a RACF user
profile after loading from YAML.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .common import RacfObject


@dataclass
class RacfUser(RacfObject):
    """
    Represents the desired state of a RACF user.

    The class intentionally does not contain:

        - RACF command syntax
        - validation rules
        - Ansible behavior

    Those responsibilities belong to other layers.
    """

    pass


def load_user(data: dict[str, Any]) -> RacfUser:
    """
    Convert YAML-loaded data into a RacfUser object.

    Expected YAML structure:

        racf_user:
            meta:
            state:
            content:

    Args:
        data:
            Dictionary produced by a YAML parser.

    Returns:
        RacfUser instance.

    Raises:
        KeyError:
            If required top-level fields are missing.
    """

    user_data = data["racf_user"]

    return RacfUser(
        state=user_data["state"],
        meta=user_data.get("meta", {}),
        content=user_data.get("content", {}),
    )
