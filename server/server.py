from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

from db import get_connection, init_db
from models import Note, Todo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

# ── NOTES ──────────────────────────────────────────

@app.post("/notes", status_code=201)
def create_note(note: Note):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (note.title, note.content)
        )
        conn.commit()
        return {"id": cur.lastrowid, "title": note.title, "content": note.content}

@app.get("/notes")
def list_notes():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, title, content FROM notes")
        rows = cur.fetchall()
        return [{"id": r["id"], "title": r["title"], "content": r["content"]} for r in rows]

# ── TODOS ──────────────────────────────────────────

@app.post("/todos", status_code=201)
def create_todo(todo: Todo):
    tasks_json = json.dumps([t.dict() for t in todo.tasks])
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO todos (title, tasks) VALUES (?, ?)",
            (todo.title, tasks_json)
        )
        conn.commit()
        return {"id": cur.lastrowid, "title": todo.title, "tasks": todo.tasks}

@app.get("/todos")
def list_todos():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, title, tasks FROM todos")
        rows = cur.fetchall()
        result = []
        for r in rows:
            try:
                tasks = json.loads(r["tasks"])
            except Exception:
                tasks = []
            result.append({"id": r["id"], "title": r["title"], "tasks": tasks})
        return result