# Notes and Todo App

Minimal notes/todo app:
- Backend: FastAPI storing notes and todos in SQLite.
- Client: Static HTML + JS calling backend.

Install & run (Mac)
1) Backend:
cd "/Users/cacia001/Documents/api key1/notes-todo-app/server"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi "uvicorn[standard]" pydantic
python -m uvicorn server:app --reload --host 127.0.0.1 --port 8000

2) Client (new terminal):
cd "/Users/cacia001/Documents/api key1/notes-todo-app/client"
python3 -m http.server 8080
open http://localhost:8080

API examples
POST create note:
curl -i -X POST http://127.0.0.1:8000/notes -H "Content-Type: application/json" -d '{"title":"t","text":"x"}'

GET notes:
curl http://127.0.0.1:8000/notes

POST create todo:
curl -i -X POST http://127.0.0.1:8000/todos -H "Content-Type: application/json" -d '{"title":"Shopping","tasks":[{"text":"Milk","completed":false}]}'

GET todos:
curl http://127.0.0.1:8000/todos