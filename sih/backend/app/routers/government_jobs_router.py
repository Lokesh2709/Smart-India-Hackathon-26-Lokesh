from fastapi import APIRouter

from app.models.government_job_models import (
    CreateGovernmentJob
)

from app.services.government_jobs_service import (
    get_all_government_jobs,
    get_job_by_id,
    get_job_skills,
    get_job_applications,
    get_matching_students,
    create_job,
    update_job_status,
    get_active_jobs
)

router = APIRouter(
    prefix="/api/government/jobs",
    tags=["Government Jobs"]
)


@router.get("/")
def jobs():

    return get_all_government_jobs()


@router.get("/active")
def active_jobs():

    return get_active_jobs()
from fastapi import Body


@router.post("/")
def create_new_job(
    payload: dict = Body(...)
):

    print("RAW PAYLOAD")
    print(payload)

    return create_job(payload)

@router.post("/test")
def test():

    return {
        "gov_rep_id": 1,
        "job_title": "Software Engineer",
        "department": "IT",
        "description": "Backend Developer",
        "location": "Bangalore",
        "salary_min": 50000,
        "salary_max": 80000,
        "application_deadline": "2026-12-31",
        "status": "ACTIVE"
    }

@router.get("/{job_id}")
def job_details(
    job_id: int
):

    return {
        "job":
            get_job_by_id(
                job_id
            ),

        "skills":
            get_job_skills(
                job_id
            ),

        "applications":
            get_job_applications(
                job_id
            )
    }


@router.get("/{job_id}/matches")
def job_matches(
    job_id: int
):

    return get_matching_students(
        job_id
    )




@router.patch(
    "/{job_id}/status"
)
def change_status(
    job_id: int,
    status: str
):

    return update_job_status(
        job_id,
        status
    )