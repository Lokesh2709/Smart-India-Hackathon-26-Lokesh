from pydantic import BaseModel
from typing import List


class DashboardSummaryResponse(BaseModel):
    total_students: int
    total_recruiters: int
    total_skills: int
    active_challenges: int
    active_government_jobs: int
    active_campaigns: int


class SkillCount(BaseModel):
    skill_name: str
    count: int


class SectorCount(BaseModel):
    sector_name: str
    count: int


class RegionCount(BaseModel):
    region: str
    count: int


class SkillGapResponse(BaseModel):
    skill_name: str
    supply: int
    demand: int
    gap: int