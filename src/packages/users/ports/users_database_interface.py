import abc
from typing import Union
from sqlalchemy.orm import Session
from packages.users.schemas.users import User


class UsersDatabaseInterface(abc.ABC):
    db_session: Session

    @abc.abstractmethod
    async def list_users(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_user(self, user_id: int) -> Union[User, None]:
        raise NotImplementedError

    @abc.abstractmethod
    async def create_user(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    async def update_user(self, user_id: int, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_user(self, user_id: int) -> int:
        raise NotImplementedError
