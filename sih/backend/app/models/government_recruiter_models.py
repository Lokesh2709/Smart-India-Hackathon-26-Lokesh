from pydantic import BaseModel


class RecruiterResponse(BaseModel):
    recruiter_id: int
    company_name: str
    industry: str