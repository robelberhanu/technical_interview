from sqlite3 import Binary
from sre_constants import IN
from sqlalchemy import Column, Integer, LargeBinary, String
from database import Base

class Info(Base):
    __tablename__ = "info"
    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name =last_name
        self.birthday = birthday

    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(String)

class ExcelData(Base):
    __tablename__ = "excel_info"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    month = Column(String)
    income = Column(Integer)
    expenses = Column(Integer)

