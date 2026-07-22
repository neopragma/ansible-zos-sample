from dataclasses import dataclass, field

# from ..operations import Operation


@dataclass(frozen=True)
class Plan:
    # Note: Avoid 'operations = list[]'. Use default_factory to ensure every instance has a unique list.
    operations: list[Operation] = field(default_factory=list)
