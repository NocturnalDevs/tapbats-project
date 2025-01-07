from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    telegramID: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    lastOnline: datetime
    referralCode: str

    class Config:
        from_attributes = True