from pydantic import BaseModel,EmailStr,field_validator 
import re

class User(BaseModel):
    username:str
    email:EmailStr
    password:str
    
    @field_validator("password",check_fields=False)
    @staticmethod
    def password_validation(cls,value):
        if len(value)<8:
            raise ValueError("a password should have at  least 8 characters")
        if not re.search(r"[A-Z]",value):
            raise ValueError(r'[0-9]',value)
        return value
    
    @field_validator("email",check_fields=False)
    @staticmethod
    def email_validation(cls,email):
        if not email.endswith("@gmail.com"):
            raise ValueError("email should with gmail.com")
        return email


class Userverify(BaseModel):
    email:EmailStr
    password:str    
    
    @field_validator("password",check_fields=False)
    @staticmethod
    def password_validation(cls,value):
        if len(value)<8:
            raise ValueError("a password should have at  least 8 characters")
        if not re.search(r"[A-Z]",value):
            raise ValueError("a password must contain at least on capital letter")
        if not re.search(r"[0-9]",value):
            raise ValueError("a password should contain at least on digit")
        return value
    
    @field_validator("email",check_fields=False)
    @staticmethod
    def email_validation(cls,email):
        if not email.endswith("@gmail.com"):
            raise ValueError("email should with gmail.com")
        return email
