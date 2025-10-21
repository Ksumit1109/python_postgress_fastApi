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
    return{"message": "Welcome to main page user"}

@app.get("/users/", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    return services.get_users(db)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)    

# @app.post("/upload")
# def handleImage(files: list[UploadFile]):
#     print(files)
#     return{"status" : "File received"}


uvicorn.run(app)