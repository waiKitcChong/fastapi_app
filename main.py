from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
import os

url = "https://gvndeepzsoohrushohdn.supabase.co"
key = "sb_secret_n6vMn7ghJ22xhICePKJErQ_1ibfx-Nm"

# Supabase config
SUPABASE_URL = os.getenv("SUPABASE_URL", url)
SUPABASE_KEY = os.getenv("SUPABASE_KEY", key)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Model
class Note(BaseModel):
    title: str
    content: str

# CREATE
@app.post("/notes")
def create_note(note: Note):
    response = supabase.table("notes").insert({
        "title": note.title,
        "content": note.content
    }).execute()
    return {"message": "Note added", "data": response.data}

# READ
@app.get("/notes")
def get_notes():
    response = supabase.table("notes").select("*").execute()
    return response.data

# UPDATE
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    response = supabase.table("notes").update({
        "title": note.title,
        "content": note.content
    }).eq("id", note_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note updated", "data": response.data}

# DELETE
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    response = supabase.table("notes").delete().eq("id", note_id).execute()
    return {"message": "Note deleted", "data": response.data}
