from dataclasses import dataclass


@dataclass(frozen=True)
class EnsureUser:
    userid: str
