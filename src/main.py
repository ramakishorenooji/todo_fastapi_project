from fastapi import FastAPI, Depends
from typing import List
from app.orm.database import engine, SessionLocal
from app.orm import models
from app.orm.schemas import Todo, TodoRequest, TodoCreate
from starlette.staticfiles import StaticFiles
from app.repositories.todo_repository_impl import TodoRepositoryImpl
from app.services.services import TodoService
from app.routes.todo import todo_router
from app.routes.users import users_router
from app.routes.admin import admin_router
from app.routes.auth import auth_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_todo_service(db=Depends(get_db)):
#     repo = TodoRepositoryImpl(db)
#     return TodoService(repo)

#Include the todo routers
app.include_router(todo_router)
app.include_router(users_router)
app.include_router(admin_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Todo API"}

# @app.get("/todos", response_model=List[Todo])
# def list_todos(service: TodoService = Depends(get_todo_service)):
#     return service.list_todos()

# @app.post("/todos", response_model=Todo)
# def create_todo(todo: TodoCreate, service: TodoService = Depends(get_todo_service)):
#     return service.add_todo(todo)