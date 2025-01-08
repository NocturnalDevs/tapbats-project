from pydantic import BaseModel
from datetime import datetime

# Base schema for User
class UserBase(BaseModel):
    telegramID: str
    lastOnline: datetime
    referralCode: str

# Schema for creating a User
class UserCreate(UserBase):
    pass

# Schema for returning a User
class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Enable ORM mode for SQLAlchemy models