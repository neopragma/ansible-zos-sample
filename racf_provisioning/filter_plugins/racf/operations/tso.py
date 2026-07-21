from dataclasses import dataclass

@dataclass(frozen=True)
class EnsureTSO:
    userid: str
    acct: str
    proc: str
