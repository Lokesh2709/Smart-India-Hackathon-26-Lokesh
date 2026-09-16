from collections import Counter

from app.database.supabase_client import supabase


from collections import Counter

from app.database.supabase_client import supabase


def get_skill_gap_analysis():

    try:

        student_skills = (
            supabase
            .table("student_skills")
            .select("*")
            .execute()
        )

        challenge_skills = (
            supabase
            .table("challenge_skills")
            .select("*")
            .execute()
        )

        student_counter = Counter()
        recruiter_counter = Counter()

        for row in student_skills.data:

            skill_id = row.get("skill_id")

            if skill_id:
                student_counter[str(skill_id)] += 1

        for row in challenge_skills.data:

            skill_id = row.get("skill_id")

            if skill_id:
                recruiter_counter[str(skill_id)] += 1

        results = []

        all_skills = (
            set(student_counter.keys())
            |
            set(recruiter_counter.keys())
        )

        for skill in all_skills:

            supply = student_counter.get(
                skill,
                0
            )

            demand = recruiter_counter.get(
                skill,
                0
            )

            results.append(
                {
                    "skill_name": f"Skill {skill}",
                    "student_supply": supply,
                    "industry_demand": demand,
                    "skill_gap": demand - supply
                }
            )

        return results

    except Exception as e:

        return [
            {
                "error": str(e)
            }
        ]

def get_regional_skill_distribution():

    students = (
        supabase
        .table("students")
        .select(
            """
            student_id,
            location
            """
        )
        .execute()
    )

    counter = Counter()

    for row in students.data:

        location = row.get(
            "location"
        )

        if location:

            counter[
                location
            ] += 1

    return [
        {
            "region": region,
            "student_count": count
        }
        for region, count
        in counter.most_common()
    ]
def get_low_pursued_sectors():

    sectors = get_sector_strengths()

    return sorted(
        sectors,
        key=lambda x: x["count"]
    )[:10]
def search_skill(skill_name):

    result = (
        supabase
        .table("skills")
        .select("*")
        .ilike(
            "skill_name",
            f"%{skill_name}%"
        )
        .execute()
    )

    return result.data
def generate_statistics_report():

    students = (
        supabase
        .table("students")
        .select(
            "student_id",
            count="exact"
        )
        .execute()
    )

    recruiters = (
        supabase
        .table("recruiters")
        .select(
            "recruiter_id",
            count="exact"
        )
        .execute()
    )

    jobs = (
        supabase
        .table("government_jobs")
        .select(
            "gov_job_id",
            count="exact"
        )
        .execute()
    )

    campaigns = (
        supabase
        .table("skill_promotion_campaigns")
        .select(
            "campaign_id",
            count="exact"
        )
        .execute()
    )

    return {
        "students":
            students.count,

        "recruiters":
            recruiters.count,

        "government_jobs":
            jobs.count,

        "campaigns":
            campaigns.count
    }

def create_campaign(payload):

    result = (
        supabase
        .table(
            "skill_promotion_campaigns"
        )
        .insert(payload)
        .execute()
    )

    return result.data
def get_sector_strengths():

    skills = (
        supabase
        .table("student_skills")
        .select(
            """
            skill_id,
            skills(
                skill_name,
                sector_name
            )
            """
        )
        .execute()
    )

    counter = Counter()

    for row in skills.data:

        if row.get("skills"):

            sector = (
                row["skills"]
                ["sector_name"]
            )

            if sector:
                counter[sector] += 1

    return [
        {
            "sector": sector,
            "count": count
        }
        for sector, count
        in counter.most_common()
    ]
def get_campaigns():

    result = (
        supabase
        .table("skill_promotion_campaigns")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return result.data