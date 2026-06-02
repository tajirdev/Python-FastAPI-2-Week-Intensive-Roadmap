from database import  Base
from sqlalchemy.orm import relationship

from sqlalchemy import Column,Integer, String, DateTime,ForeignKey
from datetime import datetime,timezone

def now_utc():
    return datetime.now(timezone.utc)

   
class User(Base):
    
    __tablename__= 'users'
    id= Column(Integer,primary_key=True)
    username = Column(String,nullable=False)
    password = Column(String,nullable=False)
    creator =relationship("note", back_populates="blog")


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at = Column(DateTime,default=now_utc)
    updated_at = Column(DateTime,default= now_utc,onupdate=now_utc)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    blog=relationship("user", back_populates="creator")   
 












