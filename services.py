from models import User
from sqlalchemy.orm import Session
from schemas import UserCreate

def create_user(db: Session, data: UserCreate):
    user_instance = User(**data.model_dump())
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return user_instance


def get_users(db: Session):
    return db.query(User).all()