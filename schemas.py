from pydantic import BaseModel
from typing import Union

class userBase(BaseModel):
    name: str
    gender: str
    email: str
    birthYear: int
    password: Union[str, int] 

class UserCreate(userBase):
    pass


class User(userBase):
    id: str

    class Config: 
        from_attributes = True  # Changed from 'from_attribute' to 'from_attributes'