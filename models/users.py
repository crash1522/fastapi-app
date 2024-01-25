from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        scheme_extra = {
            "example" : {
                "email": "example@gmail.com",
                "password": "example123",
                "events": [],
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    class Config:
        scheme_extra = {
            "example" : {
                "email": "example@gmail.com",
                "password": "example123",
                "events": [],
            }
        }