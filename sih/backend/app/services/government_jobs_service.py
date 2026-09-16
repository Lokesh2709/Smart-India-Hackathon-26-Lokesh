from app.database.supabase_client import supabase
from postgrest.exceptions import APIError


def get_all_government_jobs():

    result = (
        supabase
        .table("government_jobs")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return result.data


def get_job_by_id(job_id):

    result = (
        supabase
        .table("government_jobs")
        .select("*")
        .eq("gov_job_id", job_id)
        .execute()
    )

    if not result.data:
        return None

    return result.data[0]


def get_job_skills(job_id):

    result = (
        supabase
        .table("government_job_skills")
        .select(
            """
            *,
            skills(skill_name,sector_name)
            """
        )
        .eq("gov_job_id", job_id)
        .execute()
    )

    return result.data


def get_job_applications(job_id):

    result = (
        supabase
        .table("government_job_applications")
        .select("*")
        .eq("gov_job_id", job_id)
        .execute()
    )

    return result.data


def get_active_jobs():

    result = (
        supabase
        .table("government_jobs")
        .select("*")
        .eq("status", "ACTIVE")
        .execute()
    )

    return result.data
def get_matching_students(job_id):

    skills_result = (
        supabase
        .table("government_job_skills")
        .select("skill_id")
        .eq("gov_job_id", job_id)
        .execute()
    )

    required_skills = set(
        row["skill_id"]
        for row in skills_result.data
    )

    students_result = (
        supabase
        .table("student_skills")
        .select(
            """
            student_id,
            skill_id,
            proficiency_score
            """
        )
        .execute()
    )

    student_map = {}

    for row in students_result.data:

        sid = row["student_id"]

        if sid not in student_map:
            student_map[sid] = []

        student_map[sid].append(
            row
        )

    rankings = []

    for sid, skills in student_map.items():

        matched = 0

        total_score = 0

        for skill in skills:

            if (
                skill["skill_id"]
                in required_skills
            ):

                matched += 1

                total_score += (
                    skill.get(
                        "proficiency_score"
                    )
                    or 0
                )

        if matched > 0:

            match_score = round(
                (
                    matched
                    /
                    len(required_skills)
                ) * 100,
                2
            )

            rankings.append(
                {
                    "student_id": sid,
                    "match_score": match_score,
                    "skill_score": total_score
                }
            )

    rankings.sort(
        key=lambda x: (
            x["match_score"],
            x["skill_score"]
        ),
        reverse=True
    )

    return rankings[:50]


from postgrest.exceptions import APIError


def create_job(payload):

    print("=" * 50)
    print("PAYLOAD BEFORE INSERT")
    print(payload)
    print("=" * 50)

    try:

        result = (
            supabase
            .table("government_jobs")
            .insert(payload)
            .execute()
        )

        print("INSERT SUCCESS")
        print(result.data)

        return result.data

    except Exception as e:

        print("=" * 50)
        print("INSERT FAILED")
        print(str(e))
        print("=" * 50)

        raise e
    
def update_job_status(
    job_id,
    status
):

    result = (
        supabase
        .table("government_jobs")
        .update(
            {
                "status": status
            }
        )
        .eq(
            "gov_job_id",
            job_id
        )
        .execute()
    )

    return result.data