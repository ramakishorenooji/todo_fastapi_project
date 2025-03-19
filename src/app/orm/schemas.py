# filepath: /Users/ramakishorenooji/code/todo_fastapi_project/src/app/orm/schemas.py
from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    title: str
    description: Optional[str] = None
    priority: int = 0
    complete: bool = False
    owner_id: int

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode: True