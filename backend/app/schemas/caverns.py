from pydantic import BaseModel

class CavernBase(BaseModel):
    name: str
    description: str
    requiredProgress: float

class CavernCreate(CavernBase):
    pass

class Cavern(CavernBase):
    id: int

    class Config:
        from_attributes = True

class UserCavernBase(BaseModel):
    telegramID: str
    cavernID: int

class UserCavernCreate(UserCavernBase):
    pass

class UserCavern(UserCavernBase):
    id: int
    owned: bool
    currentProgress: float

    class Config:
        from_attributes = True