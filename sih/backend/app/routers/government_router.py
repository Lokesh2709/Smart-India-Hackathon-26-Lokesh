from fastapi import APIRouter

from app.services.government_service import (
    get_total_students,
    get_total_skills,
    get_top_skills
)

router = APIRouter(
    prefix="/api/government",
    tags=["Government"]
)


@router.get("/dashboard")
def dashboard():

    return {
        "total_students": get_total_students(),
        "total_skills": get_total_skills()
    }


@router.get("/top-skills")
def top_skills():

    return {
        "top_skills": get_top_skills()
    }