from pydantic import BaseModel

class UserBase(BaseModel):
    telegramID: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    lastOnline: str
    referralCode: str

    class Config:
        from_attributes = True