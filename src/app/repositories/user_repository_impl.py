from sqlalchemy.orm import Session
from app.orm.models import User

class UserRepositoryImpl:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(User).all()