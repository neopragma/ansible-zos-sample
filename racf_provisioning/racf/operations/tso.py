from dataclasses import dataclass


@dataclass(frozen=True)
class EnsureTSO:
    userid: str
    account_number: str | None = None
    procedure: str | None = None
    command: str | None = None
    destination: str | None = None
    hold_class: str | None = None
    job_class: str | None = None
    message_class: str | None = None
    size_max: int | None = None
    region_size: int | None = None
    unit: str | None = None
    user_data: str | None = None
