from typing import List
from sqlalchemy.orm import Session
from app.orm.schemas import Todo, TodoCreate
from app.repositories import repository


class TodoService:
    def __init__(self, repo: repository.TodoRepository):
        self.repo = repo

    def list_todos(self) -> List[Todo]:
        return self.repo.get_all_todos()

    def add_todo(self, todo: TodoCreate) -> Todo:
        return self.repo.create_todo(todo)
