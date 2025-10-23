from pydantic import BaseModel
from typing import Optional, Union

class userBase(BaseModel):
    name: str
    gender: str
    email: str
    birthYear: int
    password: Union[str, int]  # safer typing

class UserCreate(userBase):
    pass

# 👇 New class for PATCH
class UserUpdate(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    birthYear: Optional[str] = None
    password: Optional[Union[str , int]] = None


class User(userBase):
    id: str

    class Config: 
        from_attributes = True  # Changed from 'from_attribute' to 'from_attributes'