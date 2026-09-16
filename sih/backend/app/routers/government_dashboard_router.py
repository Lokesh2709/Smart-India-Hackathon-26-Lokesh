from fastapi import APIRouter

from app.services.government_dashboard_service import (
    get_dashboard_summary,
    get_top_student_skills,
    get_top_demand_skills,
    get_highest_skilled_sectors,
    get_lowest_pursued_sectors,
    get_regional_distribution,
    get_skill_gap_analysis
)

router = APIRouter(
    prefix="/api/government",
    tags=["Government Dashboard"]
)


@router.get("/dashboard-summary")
def dashboard_summary():

    return get_dashboard_summary()


@router.get("/top-student-skills")
def top_student_skills():

    return get_top_student_skills()


@router.get("/top-demand-skills")
def top_demand_skills():

    return get_top_demand_skills()


@router.get("/highest-skilled-sectors")
def highest_skilled_sectors():

    return get_highest_skilled_sectors()


@router.get("/lowest-pursued-sectors")
def lowest_pursued_sectors():

    return get_lowest_pursued_sectors()


@router.get("/regional-distribution")
def regional_distribution():

    return get_regional_distribution()


@router.get("/skill-gap")
def skill_gap():

    return get_skill_gap_analysis()