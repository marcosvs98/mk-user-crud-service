from typing import Any, Optional, Union, List
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
from packages.users.ports.users_service_inteface import UsersServiceInterface
from packages.users.schemas.users import User

USER_PARAMETER = "{user_id}"


class UsersController:
    def __init__(self, users_service: UsersServiceInterface):
        self.service = users_service
        self.router = APIRouter()
        self.router.add_api_route("/", self.list_users, methods=["GET"], response_model=List[User])
        self.router.add_api_route("/", self.create_user, methods=["POST"], response_model=User)
        self.router.add_api_route(
            f"/{USER_PARAMETER}",
            self.get_user,
            methods=["GET"],
            response_model=User
        )
        self.router.add_api_route(
            f"/{USER_PARAMETER}",
            self.delete_user,
            methods=["DELETE"]
        )
        self.router.add_api_route(
            f"/{USER_PARAMETER}",
            self.update_user,
            methods=["PUT"],
            response_model=User
        )

    async def create_user(
        self, request: Request, user: User, db_session: Session = Depends(get_db)
    ):
        self.service.repository.db_session = db_session
        return await self.service.create_user(user=user)

    async def list_users(
        self, request: Request, db_session: Session = Depends(get_db)
    ):
        self.service.repository.db_session = db_session
        return await self.service.list_users()

    async def get_user(
        self, request: Request, user_id, db_session: Session = Depends(get_db)
    ):
        self.service.repository.db_session = db_session
        return await self.service.get_user(user_id=user_id)

    async def delete_user(
        self, request: Request, user_id, db_session: Session = Depends(get_db)
    ):
        self.service.repository.db_session = db_session
        return await self.service.delete_user(user_id=user_id)

    async def update_user(
        self,
        request: Request,
        user_id,
        user: User,
        db_session: Session = Depends(get_db),
    ):
        self.service.repository.db_session = db_session
        return await self.service.update_user(
            user_id=user_id, user=user
        )
