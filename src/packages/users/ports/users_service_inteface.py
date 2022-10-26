import abc

from packages.users.ports.users_database_interface import UsersDatabaseInterface
from packages.users.schemas.users import User


class UsersServiceInterface(abc.ABC):

    repository: UsersDatabaseInterface

    @abc.abstractmethod
    def __init__(self, repository: UsersDatabaseInterface):
        raise NotImplementedError

    @abc.abstractmethod
    async def list_users(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_user(self, user_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    async def create_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    async def update_user(self, user_id: int, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_user(self, user_id: int):
        raise NotImplementedError

