from uuid import uuid4

from sqlalchemy.orm import Session
from database.models import User as UserORM
from packages.users.ports.users_database_interface import UsersDatabaseInterface  # noqa: E501
from packages.users.schemas.users import User


class UsersRepository(UsersDatabaseInterface):
    db_session: Session
    user_model = UserORM

    async def list_users(self):
        users = self.db_session.query(self.user_model)
        return [User.from_orm(user_orm) for user_orm in users.all()]

    async def get_user(self, user_id: str):
        user_orm = (
            self.db_session.query(self.user_model)
            .filter(self.user_model.id == user_id)
            .first()
        )
        return User.from_orm(user_orm) if user_orm else None

    async def create_user(self, user: User):
        db_user = self.user_model(**user.dict())
        db_user.id = str(uuid4())
        self.db_session.add(db_user)
        self.db_session.commit()
        return User.from_orm(db_user)

    async def update_user(self, user_id: str, user: User):
        db_user = (
            self.db_session.query(self.user_model)
            .filter(self.user_model.id == user_id)
            .scalar()
        )
        db_user.update(**user.dict(exclude_unset=True))
        self.db_session.commit()
        return User.from_orm(db_user)

    async def delete_user(self, user_id: str):
        result = (
            self.db_session.query(self.user_model)
            .filter(self.user_model.id == user_id)
            .delete()
        )
        self.db_session.commit()
        return result
