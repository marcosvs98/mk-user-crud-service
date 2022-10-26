from typing import Optional
from pydantic import constr, BaseModel


class User(BaseModel):
    id: Optional[constr(max_length=500)]
    email: str
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True

