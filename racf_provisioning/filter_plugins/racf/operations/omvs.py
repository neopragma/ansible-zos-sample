from dataclasses import dataclass


@dataclass(frozen=True)
class EnsureOMVS:
    userid: str
    uid: int
    home: str
    program: str
