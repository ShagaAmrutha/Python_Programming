from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def search_books(field, keyword):
    return sb.table("books").select("*").ilike(field, f"%{keyword}%").execute().data

if __name__ == "__main__":
    field = input("Search by (title/author/category): ").strip().lower()
    keyword = input("Enter search keyword: ").strip()

    results = search_books(field, keyword)
    if results:
        print("Books found:")
        for b in results:
            print(f"{b['book_id']}: {b['title']} by {b['author']} ({b['category']}) — Stock: {b['stock']}")
    else:
        print("No books found.")
