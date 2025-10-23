import uuid
from db import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    gender = Column(String, index=True)
    email = Column(String, index=True)
    birthYear = Column(Integer)
    password = Column(String(30))