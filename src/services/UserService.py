from interfaces.UserRepository import UserRepository
from typing import Optional
from models.User import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_by_email_and_password(self, email: str, password: str) -> Optional[User]:
        return self.user_repository.get_user_by_email_and_password(email, password)
