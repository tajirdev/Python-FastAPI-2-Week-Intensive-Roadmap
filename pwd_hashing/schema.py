from pydantic import Basemodel,EmailStr,field_validator 
import re

class User(Basemodel):
    username:str
    email:EmailStr
    passwoed:str
    
    @field_validator("password")
    def password_validation(cls,value):
        if len(value)<8:
            raise ValueError("a password should have at  least 8 characters")
        if not re.search(r"[A-Z]",value):
            raise ValueError(r'[0-9]',value)
        return value
    
    @field_validator("email")
    def email_validation(cls,email):
        if not email.endwith("gmail.com",email):
            raise ValueError("email should with gmail.com")
        return email