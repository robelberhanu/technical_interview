from sqlite3 import Binary
from sqlalchemy import Column, Integer, LargeBinary, String
from database import Base

class Info(Base):
    __tablename__ = "info"

    first_name = Column(String, primary_key = True, index=True)
    last_name = Column(String)
    birthday = Column(String)
    file = Column(LargeBinary)