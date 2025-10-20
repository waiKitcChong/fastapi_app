from fastapi import FastAPI
from supabase import create_client, Client

app = FastAPI()

url = "https://gvndeepzsoohrushohdn.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd2bmRlZXB6c29vaHJ1c2hvaGRuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA5NDI1NjEsImV4cCI6MjA3NjUxODU2MX0.DeZBvBV_1IRsjCx-eBIdRIvCqRi1i8Y3cnqhld2JDT8"
supabase: Client = create_client(url, key)

@app.get("/items")
def get_items():
    res = supabase.table("items").select("*").execute()
    return res.data

@app.post("/items")
def add_item(name: str, description: str):
    res = supabase.table("items").insert({"name": name, "description": description}).execute()
    return {"message": "Item added", "data": res.data}
