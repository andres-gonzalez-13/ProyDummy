from interfaces.UserInterface import UserInterface
from typing import Optional
from models.User import User

class UserService:
    def __init__(self, user_interface: UserInterface):
        self.user_interface = user_interface

    def get_user_by_email_and_password(self, email: str, password: str) -> Optional[User]:
        return self.user_interface.get_user_by_email_and_password(email, password)
    
    def create_user(self, id: str, name: str, password: str, email: str) -> User:
        return self.user_interface.create_user(id,name,password,email)
