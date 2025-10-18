from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Welcome to main page user"}

@app.get("/contact")
def read_contact():
    return{"Message": "Welcome to Contact page"}


@app.post("/upload")
def handleImage(files: list[UploadFile]):
    print(files)
    return{"status" : "File received"}


uvicorn.run(app)