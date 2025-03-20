from app.repositories.user_repository_impl import UserRepositoryImpl

class UserService:
    def __init__(self, repo: UserRepositoryImpl):
        self.repo = repo

    def list_users(self):
        return self.repo.get_all_users()