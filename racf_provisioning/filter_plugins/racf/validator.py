"""
Generic schema validator for RACF object models.

The validator operates only on schema metadata.
It has no knowledge of RACF object types.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .schema.common import Field, Section, ValueType

@dataclass
class ValidationError:
    """
    Represents one validation failure.
    """

    path: str

    message: str


@dataclass
class ValidationResult:
    """
    Result of validating a model against a schema.
    """

    valid: bool

    errors: list[ValidationError] = field(
        default_factory=list
    )

def validate(
    data: dict[str, Any],
    schema: Section,
    strict: bool = False,
) -> ValidationResult:
    """
    Validate a dictionary against a schema.

    Returns:
        ValidationResult containing success state and errors.
    """

    errors: list[ValidationError] = []

    _validate_section(
        data=data,
        schema=schema,
        path=[],
        errors=errors,
        strict=strict,
    )

    return ValidationResult(
        valid=not errors,
        errors=errors,
    )

def _validate_section(
    data: dict[str, Any],
    schema: Section,
    path: list[str],
    errors: list[ValidationError],
    strict: bool = False,
) -> None:

    """
    Validate one schema section recursively.
    """

    if not isinstance(data, dict):
        errors.append(
            ValidationError(
                path=_format_path(path),
                message=f"{_format_path(path)} must be an object"
            )
        )
    allowed = set(schema.fields) | set(schema.sections)
    if strict:
        for name in data:
            if name not in allowed:
                errors.append(
                    ValidationError(
                        path=_format_path(path + [name]),
                        message=f"{_format_path(path + [name])} unknown field"
                    )
                )    
#                _add_error(
#                    errors,
#                    path + [name],
#                    "unknown field",
#                )
    #
    # Validate fields
    #

    for name, field in schema.fields.items():
        if name not in data:
            if field.required:
                errors.append(
                    ValidationError(
                        path=_format_path(path + [name]),
                        message=f"{_format_path(path)} required field missing"
                    )
                )
            continue

        _validate_field(
        value=data[name],
        field=field,
        path=path + [name],
        errors=errors,
    )

    #
    # Validate nested sections
    #

    for name, section in schema.sections.items():
        if name not in data:
            continue

        _validate_section(
            data=data[name],
            schema=section,
            path=path + [name],
            errors=errors,
            strict=strict,
        )

def _validate_field(
    value: Any,
    field: Field,
    path: list[str],
    errors: list[ValidationError],
) -> None:

    if value is None:
        return

    if field.type == ValueType.STRING:
        _validate_string(value, path, errors)

    elif field.type == ValueType.INTEGER:
        _validate_integer(value, field, path, errors)

    elif field.type == ValueType.BOOLEAN:
        _validate_boolean(value, path, errors)

    elif field.type == ValueType.ENUM:
        _validate_enum(value, field, path, errors)

    elif field.type == ValueType.LIST:
        _validate_list(value, path, errors)

    elif field.type == ValueType.OBJECT:
        _validate_object(value, path, errors)


def _validate_boolean(
    value: Any,
    path: list[str],
    errors: list[ValidationError],
) -> None:

    if not isinstance(value, bool):
        _add_error(
            errors,
            path,
            "must be a boolean",
        ) 

def _validate_enum(
    value: Any,
    field: Field,
    path: list[str],
    errors: list[ValidationError],
) -> None:

    if value not in field.choices:
        errors.append(
        ValidationError(
            path=_format_path(path),
            message=f"{_format_path(path)} must be one of "
                    f"{field.choices}; received {value!r}"
        )
    )

def _validate_integer(
    value: Any,
    field: Field,
    path: list[str],
    errors: list[ValidationError],
) -> None:

    if not isinstance(value, int):
        _add_error(
            errors,
            path,
            "must be an integer",
        )
        return

    if field.minimum is not None and value < field.minimum:
        _add_error(
            errors,
            path,
            f"must be >= {field.minimum}",
        )

    if field.maximum is not None and value > field.maximum:
        _add_error(
            errors,
            path,
            f"must be <= {field.maximum}",
        )

def _validate_list(
    value: Any,
    path: list[str],
    errors: list[ValidationError],
) -> None:

    if not isinstance(value, list):
        errors.append(
        ValidationError(
            path=_format_path(path),
            message=f"{_format_path(path)} must be a list"
        )
    )

def _validate_object(
    value: Any,
    path: list[str],
    errors: list[ValidationError],
) -> None:

    if not isinstance(value, dict):
        errors.append(
        ValidationError(
            path=_format_path(path),
            message=f"{_format_path(path)} must be an object"
            )
        )

def _validate_string(
    value: Any,
    path: list[str],
    errors: list[ValidationError],
) -> None:

    if not isinstance(value, str):
        _add_error(
            errors,
            path,
            "must be a string",
        )

def _add_error(
    errors: list[ValidationError],
    path: list[str],
    message: str,
) -> None:

    errors.append(
        ValidationError(
            path=_format_path(path),
            message=message,
        )
    )

def _format_path(parts: list[str]) -> str:
    """
    Convert a path list into dotted notation.
    Example:
        ["content", "omvs", "uid"]
    becomes:
        content.omvs.uid
    """
    return ".".join(parts)
