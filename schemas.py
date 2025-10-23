from pydantic import BaseModel

class userBase(BaseModel):
    name: str
    gender: str
    email: str
    birthYear: int
    password: str | int


class UserCreate(userBase):
    pass


class User(userBase):
    id: int

    class Config:  # Changed from 'config' to 'Config'
        from_attributes = True  # Changed from 'from_attribute' to 'from_attributes'