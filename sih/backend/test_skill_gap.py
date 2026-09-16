from app.database.supabase_client import supabase

print("Testing student_skills...")

try:

    result = (
        supabase
        .table("student_skills")
        .select("*")
        .limit(5)
        .execute()
    )

    print("SUCCESS")
    print(result.data)

except Exception as e:

    print("ERROR")
    print(e)


print("\nTesting challenge_skills...")

try:

    result = (
        supabase
        .table("challenge_skills")
        .select("*")
        .limit(5)
        .execute()
    )

    print("SUCCESS")
    print(result.data)

except Exception as e:

    print("ERROR")
    print(e)


print("\nTesting skills...")

try:

    result = (
        supabase
        .table("skills")
        .select("*")
        .limit(5)
        .execute()
    )

    print("SUCCESS")
    print(result.data)

except Exception as e:

    print("ERROR")
    print(e)