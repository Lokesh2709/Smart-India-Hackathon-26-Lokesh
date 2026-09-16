from app.database.supabase_client import supabase


def get_total_students():
    result = supabase.table("students").select(
        "student_id",
        count="exact"
    ).execute()

    return result.count


def get_total_skills():
    result = supabase.table("skills").select(
        "skill_id",
        count="exact"
    ).execute()

    return result.count


def get_top_skills():
    result = (
        supabase.table("student_skills")
        .select(
            "skill_id, skills(skill_name)"
        )
        .execute()
    )

    rows = result.data

    counter = {}

    for row in rows:
        skill_name = row["skills"]["skill_name"]

        counter[skill_name] = (
            counter.get(skill_name, 0) + 1
        )

    sorted_skills = sorted(
        counter.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_skills[:10]