from fastapi import APIRouter
from fastapi import Query

from app.services.government_students_service import (
    get_all_students,
    get_student_by_id,
    get_student_proof,
    get_student_projects,
    get_student_profile,
    search_students
)

router = APIRouter(
    prefix="/api/government/students",
    tags=["Government Students"]
)


@router.get("/")
def students():

    return get_all_students()


@router.get("/search")
def search(
    skill: str = Query(None),
    college: str = Query(None),
    location: str = Query(None),
    graduation_year: int = Query(None),
    ai_passed: bool = Query(None)
):

    return search_students(
        skill,
        college,
        location,
        graduation_year,
        ai_passed
    )


@router.get("/{student_id}")
def student_details(
    student_id: int
):

    return {
        "student": get_student_by_id(
            student_id
        ),
        "profile": get_student_profile(
            student_id
        )
    }


@router.get("/{student_id}/proof")
def student_proof(
    student_id: int
):

    return get_student_proof(
        student_id
    )


@router.get("/{student_id}/projects")
def student_projects(
    student_id: int
):

    return get_student_projects(
        student_id
    )