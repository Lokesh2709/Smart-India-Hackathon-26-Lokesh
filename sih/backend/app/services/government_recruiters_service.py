from collections import Counter

from app.database.supabase_client import supabase


def get_all_recruiters():

    result = (
        supabase
        .table("recruiters")
        .select("*")
        .execute()
    )

    return result.data


def get_recruiter_by_id(
    recruiter_id: int
):

    result = (
        supabase
        .table("recruiters")
        .select("*")
        .eq(
            "recruiter_id",
            recruiter_id
        )
        .execute()
    )

    if not result.data:
        return None

    return result.data[0]


def get_all_challenges():

    result = (
        supabase
        .table(
            "sponsored_challenges"
        )
        .select("*")
        .execute()
    )

    return result.data


def get_challenges_by_recruiter(
    recruiter_id: int
):

    result = (
        supabase
        .table(
            "sponsored_challenges"
        )
        .select("*")
        .eq(
            "recruiter_id",
            recruiter_id
        )
        .execute()
    )

    return result.data


def get_industry_demand():

    recruiters = (
        supabase
        .table("recruiters")
        .select(
            "industry"
        )
        .execute()
    )

    counter = Counter()

    for row in recruiters.data:

        industry = row.get(
            "industry"
        )

        if industry:
            counter[industry] += 1

    return [
        {
            "industry": industry,
            "count": count
        }
        for industry, count
        in counter.most_common()
    ]


def get_company_demand():

    challenges = (
        supabase
        .table(
            "sponsored_challenges"
        )
        .select(
            """
            recruiter_id
            """
        )
        .execute()
    )

    recruiters = (
        supabase
        .table(
            "recruiters"
        )
        .select(
            "recruiter_id,company_name"
        )
        .execute()
    )

    company_map = {}

    for recruiter in recruiters.data:

        company_map[
            recruiter["recruiter_id"]
        ] = recruiter[
            "company_name"
        ]

    counter = Counter()

    for challenge in challenges.data:

        recruiter_id = challenge.get(
            "recruiter_id"
        )

        company = company_map.get(
            recruiter_id
        )

        if company:
            counter[company] += 1

    return [
        {
            "company": company,
            "active_challenges": count
        }
        for company, count
        in counter.most_common()
    ]


def get_top_recruiter_skills():

    challenge_skills = (
        supabase
        .table(
            "challenge_skills"
        )
        .select(
            """
            skill_id,
            skills(skill_name)
            """
        )
        .execute()
    )

    counter = Counter()

    for row in challenge_skills.data:

        if row.get("skills"):

            skill_name = (
                row["skills"]
                ["skill_name"]
            )

            counter[
                skill_name
            ] += 1

    return [
        {
            "skill_name": skill,
            "count": count
        }
        for skill, count
        in counter.most_common(20)
    ]