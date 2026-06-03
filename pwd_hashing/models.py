from database import Base
from sqlalchemy import Column,Integer,String
from datetime import datetime

class User(Base):
    __Tablename__ = "users_table"
    
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True,nullable=True)
    email = Column(String,unique=True,nullable=True)
    passwrd  = Column(String.nullable)
    created_at = Column(datetime.now )
    id = Column(Integer,primary_key = True)