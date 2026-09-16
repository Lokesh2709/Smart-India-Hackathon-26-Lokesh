from app.database.supabase_client import supabase

def get_gov_rep_by_email(
    email: str
):

    response = (
        supabase
        .table("government_representatives")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]