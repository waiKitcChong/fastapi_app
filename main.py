from fastapi import FastAPI
from supabase import create_client, Client

app = FastAPI()

url = "https://YOUR-PROJECT-URL.supabase.co"
key = "YOUR-ANON-KEY"
supabase: Client = create_client(url, key)

@app.get("/items")
def get_items():
    res = supabase.table("items").select("*").execute()
    return res.data

@app.post("/items")
def add_item(name: str, description: str):
    res = supabase.table("items").insert({"name": name, "description": description}).execute()
    return {"message": "Item added", "data": res.data}
