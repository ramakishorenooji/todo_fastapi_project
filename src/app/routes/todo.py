from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services.services import TodoService
from app.orm.schemas import TodoRequest
from app.repositories.todo_repository_impl import TodoRepositoryImpl
from app.orm.database import SessionLocal
from .auth import get_current_user

templates = Jinja2Templates(directory="templates")

todo_router = APIRouter(
    prefix='/todos',
    tags=['todos']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_todo_service(db=Depends(get_db)):
    repo = TodoRepositoryImpl(db)
    return TodoService(repo)

def redirect_to_login():
    redirect_response = RedirectResponse(url="/auth/login-page", status_code=status.HTTP_302_FOUND)
    redirect_response.delete_cookie(key="access_token")
    return redirect_response

### Pages ###
@todo_router.get("/todo-page")
async def render_todo_page(request: Request, service: TodoService = Depends(get_todo_service)):
    try:
        user = await get_current_user(request.cookies.get('access_token'))

        if user is None:
            return redirect_to_login()

        todos = service.list_todos_by_user(user.get("id"))
        return templates.TemplateResponse("todo.html", {"request": request, "todos": todos, "user": user})

    except:
        return redirect_to_login()

@todo_router.get("/edit-todo-page/{todo_id}")
async def render_edit_todo_page(request: Request, todo_id: int, service: TodoService = Depends(get_todo_service)):
    try:
        user = await get_current_user(request.cookies.get('access_token'))

        if user is None:
            return redirect_to_login()

        todo = service.get_todo_by_id(todo_id, user.get("id"))
        return templates.TemplateResponse("edit-todo.html", {"request": request, "todo": todo, "user": user})

    except:
        return redirect_to_login()

### Endpoints ###
@todo_router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: dict = Depends(get_current_user), service: TodoService = Depends(get_todo_service)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return service.list_todos_by_user(user.get('id'))

@todo_router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(todo_id: int, user: dict = Depends(get_current_user), service: TodoService = Depends(get_todo_service)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return service.get_todo_by_id(todo_id, user.get('id'))

@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_request: TodoRequest, user: dict = Depends(get_current_user), service: TodoService = Depends(get_todo_service)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return service.add_todo(todo_request, user.get('id'))

@todo_router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo_id: int, todo_request: TodoRequest, user: dict = Depends(get_current_user), service: TodoService = Depends(get_todo_service)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    service.update_todo(todo_id, todo_request, user.get('id'))

@todo_router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, user: dict = Depends(get_current_user), service: TodoService = Depends(get_todo_service)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    service.delete_todo(todo_id, user.get('id'))