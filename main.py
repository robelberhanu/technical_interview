from typing import Optional
from sqlite3 import Binary
from unicodedata import name
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session 
from fastapi import FastAPI, Request, Body, File, UploadFile, Form, Depends
import plot

app = FastAPI()

models.Base.metadata.create_all(bind=engine) # create database and table if it does not already exist


templates = Jinja2Templates(directory="templates")
mylist = []


#utility function to handle the opening and closing of database engine automatically
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# structure user input
class FormData(BaseModel):
    first_name : str
    last_name : str
    birthday : str
    # filename : bytes

# render home page
@app.get("/home", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

# Endpoit to read database
@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Info).all()


# Endpoit for submitting form data
@app.post("/submitform")
def add_info(formData: FormData, filename: UploadFile = File(...),db: Session = Depends(get_db)):
    info_model = models.Info()
    info_model.first_name = formData.first_name
    info_model.last_name = formData.last_name
    info_model.birthday = formData.birthday
    # info_model.file = formData.filename

    db.add(info_model)
    db.add(filename)
    db.commit()

    return formData









