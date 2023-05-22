from typing import Optional
from models.User import User

class UserInterface:
    def get_user_by_email_and_password(self, email: str, password: str) -> Optional[User]:
        raise NotImplementedError