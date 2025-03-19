from abc import ABC, abstractmethod
from typing import List
from app.orm import models
from app.orm.schemas import TodoCreate, Todo


class TodoRepository(ABC):
    @abstractmethod
    def get_all_todos(self) -> List[Todo]:
        pass

    @abstractmethod
    def create_todo(self, todo: TodoCreate) -> Todo:
        pass