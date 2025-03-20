from typing import List
from app.orm.schemas import Todo, TodoCreate, TodoRequest
from app.repositories.repository import TodoRepository

class TodoService:
    def __init__(self, repo: TodoRepository):
        self.repo = repo

    def list_todos(self) -> List[Todo]:
        return self.repo.get_all_todos()

    def list_todos_by_user(self, user_id: int) -> List[Todo]:
        return self.repo.get_todos_by_user(user_id)

    def get_todo_by_id(self, todo_id: int, user_id: int) -> Todo:
        return self.repo.get_todo_by_id(todo_id, user_id)

    def add_todo(self, todo_request: TodoRequest, user_id: int) -> Todo:
        return self.repo.create_todo(todo_request, user_id)

    def update_todo(self, todo_id: int, todo_request: TodoRequest, user_id: int):
        self.repo.update_todo(todo_id, todo_request, user_id)

    def delete_todo(self, todo_id: int, user_id: int):
        self.repo.delete_todo(todo_id, user_id)
