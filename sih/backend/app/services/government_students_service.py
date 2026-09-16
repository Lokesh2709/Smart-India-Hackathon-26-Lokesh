from app.database.supabase_client import supabase

def get_all_students():

    result = (
        supabase
        .table("students")
        .select("*")
        .limit(10)
        .execute()
    )

    return result.data

def get_all_students():

    result = (
        supabase
        .table("candidate_search_view")
        .select("*")
        .execute()
    )

    return result.data


def get_student_by_id(student_id: int):

    result = (
        supabase
        .table("students")
        .select("*")
        .eq("student_id", student_id)
        .execute()
    )

    print(result.data)

    if not result.data:
        return None

    return result.data[0]
def get_student_proof(student_id: int):

    result = (
        supabase
        .table("candidate_proof_view")
        .select("*")
        .eq("student_id", student_id)
        .execute()
    )

    return result.data


def get_student_projects(student_id: int):

    result = (
        supabase
        .table("student_projects")
        .select("*")
        .eq("student_id", student_id)
        .execute()
    )

    return result.data


def get_student_profile(student_id: int):

    result = (
        supabase
        .table("student_profiles")
        .select("*")
        .eq("student_id", student_id)
        .execute()
    )

    if not result.data:
        return None

    return result.data[0]


def search_students(
    skill=None,
    college=None,
    location=None,
    graduation_year=None,
    ai_passed=None
):

    query = (
        supabase
        .table("candidate_search_view")
        .select("*")
    )

    if college:
        query = query.ilike(
            "college_name",
            f"%{college}%"
        )

    if location:
        query = query.ilike(
            "location",
            f"%{location}%"
        )

    if graduation_year:
        query = query.eq(
            "graduation_year",
            graduation_year
        )

    if ai_passed is not None:
        query = query.eq(
            "ai_test_passed",
            ai_passed
        )

    result = query.execute()

    rows = result.data

    if skill:

        filtered = []

        for row in rows:

            skills = row.get(
                "skills",
                []
            )

            if not skills:
                continue

            skills_lower = [
                str(x).lower()
                for x in skills
            ]

            if skill.lower() in skills_lower:
                filtered.append(row)

        return filtered

    return rows