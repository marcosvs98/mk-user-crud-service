from sqlalchemy import Column, String, Integer
try:
    from database.base_model import ORMBaseModel
except ModuleNotFoundError:
    from base_model import ORMBaseModel


class User(ORMBaseModel):
    __name__ = 'users'

    id = Column(String(500), primary_key=True, index=True)
    email = Column(String(300), unique=True)
    first_name = Column(String(300), nullable=True)
    last_name = Column(String(300), nullable=True)
    age = Column(Integer)
