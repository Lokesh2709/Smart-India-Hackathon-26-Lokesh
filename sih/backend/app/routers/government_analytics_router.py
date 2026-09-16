from fastapi import APIRouter

from app.models.government_campaign_models import (
    CreateCampaign
)

from app.services.government_analytics_service import (
    get_skill_gap_analysis,
    get_regional_skill_distribution,
    get_sector_strengths,
    get_low_pursued_sectors,
    search_skill,
    generate_statistics_report,
    get_campaigns,
    create_campaign
)

router = APIRouter(
    prefix="/api/government/analytics",
    tags=["Government Analytics"]
)


@router.get("/skill-gap")
def skill_gap():

    return get_skill_gap_analysis()


@router.get("/regional-distribution")
def regional_distribution():

    return (
        get_regional_skill_distribution()
    )


@router.get("/highest-skilled-sectors")
def highest_skilled_sectors():

    return get_sector_strengths()


@router.get("/lowest-skilled-sectors")
def lowest_skilled_sectors():

    return get_low_pursued_sectors()


@router.get("/search-skill")
def search_required_skill(
    skill_name: str
):

    return search_skill(
        skill_name
    )


@router.get("/reports")
def reports():

    return generate_statistics_report()


@router.get("/campaigns")
def campaigns():

    return get_campaigns()


@router.post("/campaigns")
def add_campaign(
    request: CreateCampaign
):

    return create_campaign(
        request.model_dump()
    )