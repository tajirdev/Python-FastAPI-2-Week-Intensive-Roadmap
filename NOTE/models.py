from database import Base
from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users_table"
    
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True,nullable=True)
    email = Column(String,unique=True,nullable=True)
    password  = Column(String,nullable=True)
    created_at = Column(DateTime,default=datetime.now )