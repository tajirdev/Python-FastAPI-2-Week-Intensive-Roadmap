from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


#user schemas
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr

class UserResponse(BaseModel):
    username: str
    email: EmailStr

    class Config:
        from_attributes = True




#note schemas
class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    user_id: int

class NoteUpdate(BaseModel):
    title: str = Field(None, min_length=1)
    content: str = Field(None, min_length=1)

class NoteResponse(BaseModel):
    title: str
    content: str
    

    class Config:
        from_attributes = True
