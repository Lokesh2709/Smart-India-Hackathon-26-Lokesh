# test_connection.py

from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")

supabase = create_client(url, key)

result = (
    supabase
    .table("students")
    .select("*")
    .limit(1)
    .execute()
)

print(result.data)