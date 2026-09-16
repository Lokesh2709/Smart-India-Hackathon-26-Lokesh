from collections import Counter

from app.database.supabase_client import supabase


def get_dashboard_summary():

    students = (
        supabase.table("students")
        .select("student_id", count="exact")
        .execute()
    )

    recruiters = (
        supabase.table("recruiters")
        .select("recruiter_id", count="exact")
        .execute()
    )

    skills = (
        supabase.table("skills")
        .select("skill_id", count="exact")
        .execute()
    )

    challenges = (
        supabase.table("sponsored_challenges")
        .select("challenge_id", count="exact")
        .eq("challenge_status", "Active")
        .execute()
    )

    jobs = (
        supabase.table("government_jobs")
        .select("gov_job_id", count="exact")
        .eq("status", "Active")
        .execute()
    )

    campaigns = (
        supabase.table("skill_promotion_campaigns")
        .select("campaign_id", count="exact")
        .execute()
    )

    return {
        "total_students": students.count or 0,
        "total_recruiters": recruiters.count or 0,
        "total_skills": skills.count or 0,
        "active_challenges": challenges.count or 0,
        "active_government_jobs": jobs.count or 0,
        "active_campaigns": campaigns.count or 0
    }


def get_top_student_skills(limit=5):

    result = (
        supabase.table("student_skills")
        .select("skill_id, skills(skill_name)")
        .execute()
    )

    counter = Counter()

    for row in result.data:

        if row.get("skills"):

            skill_name = row["skills"]["skill_name"]

            counter[skill_name] += 1

    return [
        {
            "skill_name": skill,
            "count": count
        }
        for skill, count in counter.most_common(limit)
    ]


def get_top_demand_skills(limit=5):

    result = (
        supabase.table("challenge_skills")
        .select("skill_id, skills(skill_name)")
        .execute()
    )

    counter = Counter()

    for row in result.data:

        if row.get("skills"):

            skill_name = row["skills"]["skill_name"]

            counter[skill_name] += 1

    return [
        {
            "skill_name": skill,
            "count": count
        }
        for skill, count in counter.most_common(limit)
    ]


def get_highest_skilled_sectors():

    result = (
        supabase.table("student_skills")
        .select(
            """
            skill_id,
            skills(
                sector_name
            )
            """
        )
        .execute()
    )

    counter = Counter()

    for row in result.data:

        if row.get("skills"):

            sector = row["skills"]["sector_name"]

            if sector:
                counter[sector] += 1

    return [
        {
            "sector_name": sector,
            "count": count
        }
        for sector, count
        in counter.most_common(10)
    ]


def get_lowest_pursued_sectors():

    result = (
        supabase.table("student_skills")
        .select(
            """
            skill_id,
            skills(
                sector_name
            )
            """
        )
        .execute()
    )

    counter = Counter()

    for row in result.data:

        if row.get("skills"):

            sector = row["skills"]["sector_name"]

            if sector:
                counter[sector] += 1

    sorted_sectors = sorted(
        counter.items(),
        key=lambda x: x[1]
    )

    return [
        {
            "sector_name": sector,
            "count": count
        }
        for sector, count
        in sorted_sectors[:10]
    ]


def get_regional_distribution():

    result = (
        supabase.table("students")
        .select("location")
        .execute()
    )

    counter = Counter()

    for row in result.data:

        region = row.get("location")

        if region:
            counter[region] += 1

    return [
        {
            "region": region,
            "count": count
        }
        for region, count
        in counter.most_common()
    ]


def get_skill_gap_analysis():

    supply_result = (
        supabase.table("student_skills")
        .select("skill_id, skills(skill_name)")
        .execute()
    )

    demand_result = (
        supabase.table("challenge_skills")
        .select("skill_id, skills(skill_name)")
        .execute()
    )

    supply_counter = Counter()
    demand_counter = Counter()

    for row in supply_result.data:

        if row.get("skills"):

            skill = row["skills"]["skill_name"]

            supply_counter[skill] += 1

    for row in demand_result.data:

        if row.get("skills"):

            skill = row["skills"]["skill_name"]

            demand_counter[skill] += 1

    all_skills = set(
        list(supply_counter.keys()) +
        list(demand_counter.keys())
    )

    response = []

    for skill in all_skills:

        supply = supply_counter.get(skill, 0)

        demand = demand_counter.get(skill, 0)

        response.append(
            {
                "skill_name": skill,
                "supply": supply,
                "demand": demand,
                "gap": demand - supply
            }
        )

    response.sort(
        key=lambda x: x["gap"],
        reverse=True
    )

    return response