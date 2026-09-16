from app.database.supabase_client import supabase

try:
    result = (
        supabase
        .table("students")
        .select("*")
        .limit(1)
        .execute()
    )

    print("SUCCESS")
    print(result.data)

except Exception as e:
    print("ERROR")
    print(e)