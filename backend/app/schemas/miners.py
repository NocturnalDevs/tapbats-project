from pydantic import BaseModel

class MinerBase(BaseModel):
    name: str
    description: str
    mineAmountPerSec: float
    levelUpGemRequirement: float
    requiredProgress: float

class MinerCreate(MinerBase):
    pass

class Miner(MinerBase):
    id: int

    class Config:
        from_attributes = True

class UserMinerBase(BaseModel):
    telegramID: str
    minerID: int

class UserMinerCreate(UserMinerBase):
    pass

class UserMiner(UserMinerBase):
    id: int
    owned: bool
    currentLevel: int
    currentProgress: float

    class Config:
        from_attributes = True