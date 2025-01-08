from pydantic import BaseModel

# Base schema for Cavern
class CavernBase(BaseModel):
    name: str
    description: str
    requiredProgress: float

# Schema for creating Cavern
class CavernCreate(CavernBase):
    pass

# Schema for returning Cavern
class Cavern(CavernBase):
    id: int

    class Config:
        from_attributes = True

# Base schema for UserCaverns
class UserCavernsBase(BaseModel):
    telegramID: str
    cavernID: int
    owned: bool
    currentProgress: float

# Schema for creating UserCaverns
class UserCavernsCreate(UserCavernsBase):
    pass

# Schema for returning UserCaverns
class UserCaverns(UserCavernsBase):
    id: int

    class Config:
        from_attributes = True