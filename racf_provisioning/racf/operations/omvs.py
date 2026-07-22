from dataclasses import dataclass


@dataclass(frozen=True)
class EnsureOMVS:
    userid: str

    uid: int

    home: str

    program: str

    cpu_time_max: int | None = None
    assize_max: int | None = None
    fileproc_max: int | None = None
    mmap_area_max: int | None = None
    threads_max: int | None = None
    proc_user_max: int | None = None
    shared_memory_max: int | None = None
    region_size_max: int | None = None
    ipc_message_queue_max: int | None = None
    ipc_semaphore_max: int | None = None
    ipc_shared_memory_max: int | None = None
