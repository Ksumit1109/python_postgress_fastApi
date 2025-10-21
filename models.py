from db import Base
from sqlalchemy import Integer, Column, String

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    gender = Column(String, index=True)
    email = Column(String, index=True)
    birthYear = Column(Integer)