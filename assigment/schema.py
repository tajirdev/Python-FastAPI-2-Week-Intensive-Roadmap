from pydantic import BaseModel,Field


class User(BaseModel):  
   username:str
   password:str

class Note(BaseModel):
   title:str= Field(min_length=1)
   content:str=Field(min_length=10)
   user_id:int

    
    
    
    
    
    
    
    
    
    
    
    
    
    