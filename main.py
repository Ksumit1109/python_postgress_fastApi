from fastapi import FastAPI, Depends, HTTPException
import uvicorn
import services, models, schemas
from db import get_db, engine, create_table
from sqlalchemy.orm import Session

app = FastAPI()

# Create tables on startup
@app.on_event("startup")
def startup_event():
    create_table()

@app.get("/")
def read_root():
    return{"message": "Welcome to Main page"}

@app.get("/users/", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    return services.get_users(db)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)    


# 👇 PATCH route
@app.patch('/users/{user_id}',  response_model=schemas.User)
def path_user(user_id: str, updates: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_user = services.update_user(db, user_id, updates)
    if not updated_user:
        raise HTTPException(status_code=404, detail="user not found")
    return updated_user


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)