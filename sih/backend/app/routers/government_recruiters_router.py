from fastapi import APIRouter

from app.services.government_recruiters_service import (
    get_all_recruiters,
    get_recruiter_by_id,
    get_all_challenges,
    get_challenges_by_recruiter,
    get_industry_demand,
    get_company_demand,
    get_top_recruiter_skills
)

router = APIRouter(
    prefix="/api/government/recruiters",
    tags=[
        "Government Recruiters"
    ]
)


@router.get("/")
def recruiters():

    return get_all_recruiters()


@router.get("/industry-demand")
def industry_demand():

    return get_industry_demand()


@router.get("/company-demand")
def company_demand():

    return get_company_demand()


@router.get("/top-skills")
def top_skills():

    return get_top_recruiter_skills()


@router.get("/challenges")
def challenges():

    return get_all_challenges()


@router.get("/{recruiter_id}")
def recruiter(
    recruiter_id: int
):

    return {
        "recruiter":
            get_recruiter_by_id(
                recruiter_id
            ),

        "challenges":
            get_challenges_by_recruiter(
                recruiter_id
            )
    }