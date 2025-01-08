from pydantic import BaseModel

# Base schema for Miner
class MinerBase(BaseModel):
    name: str
    description: str
    mineAmountPerSec: float
    levelUpGemRequirement: float
    requiredProgress: float

# Schema for creating Miner
class MinerCreate(MinerBase):
    pass

# Schema for returning Miner
class Miner(MinerBase):
    id: int

    class Config:
        from_attributes = True

# Base schema for UserMiners
class UserMinersBase(BaseModel):
    telegramID: str
    minerID: int
    owned: bool
    currentLevel: int
    currentProgress: float

# Schema for creating UserMiners
class UserMinersCreate(UserMinersBase):
    pass

# Schema for returning UserMiners
class UserMiners(UserMinersBase):
    id: int

    class Config:
        from_attributes = True