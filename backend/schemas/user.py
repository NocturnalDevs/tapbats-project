from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    language_code: str | None = None
    is_premium: bool | None = None

class UserCreate(UserBase):
    referral_code: str | None = None

class User(UserBase):
    class Config:
        orm_mode = True