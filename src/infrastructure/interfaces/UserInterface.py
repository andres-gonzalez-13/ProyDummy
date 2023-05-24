from typing import Optional
from domainBusines.User import User


class UserInterface:
    def get_user_by_email_and_password(self, email: str, password: str) -> Optional[User]:
        raise NotImplementedError
    
    def create_user(self, id: str, name: str, password: str, email: str) -> User:
        raise NotImplementedError