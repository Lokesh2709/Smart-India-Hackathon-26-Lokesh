from pydantic import BaseModel
from typing import Optional


class StudentFilterRequest(BaseModel):

    skill: Optional[str] = None
    college: Optional[str] = None
    location: Optional[str] = None
    graduation_year: Optional[int] = None
    ai_passed: Optional[bool] = None