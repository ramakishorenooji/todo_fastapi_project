from sqlalchemy.orm import Session
from app.repositories.repository import TodoRepository
from app.orm import models
from app.orm.schemas import TodoCreate

class TodoRepositoryImpl(TodoRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_todos(self):
        return self.db.query(models.Todos).all()
    
    def create_todo(self, todo: TodoCreate):
        db_todo = models.Todos(**todo.dict())
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo
    