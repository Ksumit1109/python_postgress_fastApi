from models import User
from sqlalchemy.orm import Session
from schemas import UserCreate, UserUpdate

def create_user(db: Session, data: UserCreate):
    user_instance = User(**data.model_dump())
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return user_instance


def get_users(db: Session):
    return db.query(User).all()


def update_user(db: Session, user_id: str, updates: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user