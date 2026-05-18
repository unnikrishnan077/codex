from dataclasses import dataclass


@dataclass
class JobProgress:
    job_id: int
    status: str
    detail: str
