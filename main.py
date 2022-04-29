from importlib.resources import contents
from typing import Optional
from sqlite3 import Binary
from unicodedata import name
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import models
import plot
from database import engine, SessionLocal
from sqlalchemy.orm import Session 
from fastapi import FastAPI, Request, Body, File, UploadFile, Form, Depends
import pandas as pd
import itertools
import os


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

#utility function to open and read file.
def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        



# structure user input
class FormData(BaseModel):
    first_name : str
    last_name : str
    birthday : str

    class Config:
        orm_mode = True

# render home page
@app.get("/home", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


# Endpoit for submitting form data
@app.post("/submitform")
async def add_info(filename: UploadFile = File(...),first_name: str = Form(...), last_name: str = Form(...), birthday: str = Form(...), db: Session = Depends(get_db)):


    user = models.Info(first_name = first_name ,last_name = last_name , birthday =birthday)
    db.add(user)
    db.commit()
    
    file = await filename.read()
    save_file(filename.filename, file)

    excel_data = pd.read_excel(filename.filename)
    Month = list(excel_data['Month'])
    Income = list(excel_data['Income'])
    Expenses = list(excel_data['Expenses'])

    for count, item in enumerate(Month):
        data = models.ExcelData(user_id = user.id, month = item, income = Income[count], expenses = Expenses[count])
        db.add(data)
        db.commit()

    remove_file(filename.filename)



    return {'msg':'done'}









