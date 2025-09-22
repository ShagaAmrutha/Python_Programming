from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()
sb = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def delete_book(book_id):
    borrowed = sb.table("borrow_records").select("*").eq("book_id", book_id).eq("return_date", None).execute().data
    if borrowed:  # book is currently borrowed
        return None
    return sb.table("books").delete().eq("book_id", book_id).execute().data

if __name__ == "__main__":
    bid = int(input("Enter book_id to delete: ").strip())
    confirm = input(f"Are you sure you want to delete book {bid}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted = delete_book(bid)
        if deleted:
            print("Deleted:", deleted)
        else:
            print("Cannot delete — book is borrowed or does not exist.")
    else:
        print("Delete cancelled.")
