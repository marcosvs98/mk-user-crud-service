from packages.users.ports.users_database_interface import UsersDatabaseInterface
from packages.users.ports.users_service_inteface import UsersServiceInterface
from packages.users.schemas.users import User


class UsersService(UsersServiceInterface):
    def __init__(self, repository: UsersDatabaseInterface):
        self.repository = repository

    async def list_users(self):
        return await self.repository.list_users()

    async def get_user(self, user_id: str):
        return await self.repository.get_user(user_id=user_id)

    async def create_user(self, user: User):
        return await self.repository.create_user(user)

    async def update_user(self, user_id: str, user: User):
        return await self.repository.update_user(user_id=user_id, user=user)

    async def delete_user(self, user_id: str):
        return await self.repository.delete_user(user_id=user_id)
