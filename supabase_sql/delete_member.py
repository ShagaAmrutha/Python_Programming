from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()
sb = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def delete_member(member_id):
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).eq("return_date", None).execute().data
    if borrowed:  # has active borrowed books
        return None
    return sb.table("members").delete().eq("member_id", member_id).execute().data

if __name__ == "__main__":
    mid = int(input("Enter member_id to delete: ").strip())
    confirm = input(f"Are you sure you want to delete member {mid}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted = delete_member(mid)
        if deleted:
            print("Deleted:", deleted)
        else:
            print("Cannot delete — member has borrowed books or does not exist.")
    else:
        print("Delete cancelled.")
