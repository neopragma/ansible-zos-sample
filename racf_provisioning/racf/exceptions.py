"""
Exceptions used by the RACF provisioning framework.
"""


class RacfError(Exception):
    """
    Base exception for all RACF provisioning errors.
    """


class SchemaValidationError(RacfError):
    """
    Raised when a RACF profile does not conform to the schema.
    """


class ModelError(RacfError):
    """
    Raised when YAML data cannot be converted into a RACF model object.
    """


class PlanningError(RacfError):
    """
    Raised when a desired state cannot be converted into a valid operation plan.
    """


class RenderingError(RacfError):
    """
    Raised when an operation cannot be rendered into RACF commands.
    """
