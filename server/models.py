from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    text: str
    completed: bool = False

class Note(BaseModel):
    title: str
    content: str

class Todo(BaseModel):
    title: str
    tasks: List[Task] = []
