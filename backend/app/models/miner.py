from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Miner(Base):
    __tablename__ = "miner"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    mineAmountPerSec = Column(Float)
    levelUpGemRequirement = Column(Float)
    requiredProgress = Column(Float)

class UserMiners(Base):
    __tablename__ = "user_miners"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    minerID = Column(Integer, ForeignKey("miner.id"))
    owned = Column(Boolean, default=False)
    currentLevel = Column(Integer, default=1)
    currentProgress = Column(Float, default=0)

    user = relationship("User", back_populates="miners")
    miner = relationship("Miner")