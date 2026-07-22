from pathlib import Path
import yaml
from .schema import USER_SCHEMA
from .validator import validate
from .planner import plan
from .renderer import render
from .loader import load_yaml, extract_profile

def generate_commands(document):
    result = validate(
        document,
        USER_SCHEMA,
    )

    if not result.valid:
        raise ValueError(
            format_validation_errors(result)
        )

    plan_result = plan(document)

    commands = []

    for operation in plan_result.operations:
        commands.extend(
            render(operation)
        )

    return commands

def generate_commands_from_file(filename):
    document = load_yaml(filename)
    model = extract_profile(document)
    return generate_commands(model)

def format_validation_errors(result):
    return "\n".join(
        f"{error.path}: {error.message}"
        for error in result.errors
    )
