from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def get_member(member_id):
    return sb.table("members").select("*").eq("member_id", member_id).execute().data

def get_borrowed(member_id):
    return sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data

if __name__ == "__main__":
    member_id = input("Enter member ID: ").strip()
    member = get_member(member_id)

    if member:
        m = member[0]
        print(f"Member: {m['name']} ({m['email']}) — Joined: {m['join_date']}")
        borrowed = get_borrowed(member_id)
        if borrowed:
            print("Borrowed Books:")
            for b in borrowed:
                print(f"Record {b['record_id']} → Book {b['book_id']} | Borrowed: {b['borrow_date']} | Returned: {b['return_date']}")
        else:
            print("No borrowed books.")
    else:
        print("Member not found.")
