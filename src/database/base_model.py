from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class ORMBaseModel:
    id = Column(String, primary_key=True, index=True)
    __name__: str

    def update(self, **fields):
        for key, value in fields.items():
            if hasattr(self, key):
                setattr(self, key, value)

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
