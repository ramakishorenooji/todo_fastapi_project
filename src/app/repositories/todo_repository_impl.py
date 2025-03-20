from sqlalchemy.orm import Session
from app.orm.models import Todos
from app.orm.schemas import TodoRequest

class TodoRepositoryImpl:
    def __init__(self, db: Session):
        self.db = db

    def get_all_todos(self):
        return self.db.query(Todos).all()

    def get_todos_by_user(self, user_id: int):
        return self.db.query(Todos).filter(Todos.owner_id == user_id).all()

    def get_todo_by_id(self, todo_id: int, user_id: int):
        return self.db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user_id).first()

    def create_todo(self, todo_request: TodoRequest, user_id: int):
        todo_model = Todos(**todo_request.model_dump(), owner_id=user_id)
        self.db.add(todo_model)
        self.db.commit()
        self.db.refresh(todo_model)
        return todo_model

    def update_todo(self, todo_id: int, todo_request: TodoRequest, user_id: int):
        todo_model = self.get_todo_by_id(todo_id, user_id)
        if todo_model:
            todo_model.title = todo_request.title
            todo_model.description = todo_request.description
            todo_model.priority = todo_request.priority
            todo_model.complete = todo_request.complete
            self.db.commit()

    def delete_todo(self, todo_id: int, user_id: int):
        self.db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user_id).delete()
        self.db.commit()
