from pydantic import BaseModel
from typing import Optional
from datetime import date

class CreateGovernmentJob(
    BaseModel
):
    gov_rep_id: int
    job_title: str
    department: str
    description: str
    location: str

    salary_min: float
    salary_max: float

    application_deadline: date

    status: str = "ACTIVE"