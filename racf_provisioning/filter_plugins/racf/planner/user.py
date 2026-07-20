from . import base
from . import omvs
from .common import Plan


def plan(model):

    operations = []

    operations.extend(
        base.plan(model)
    )

    operations.extend(
        omvs.plan(model)
    )

    return Plan(
        operations=operations,
    )
