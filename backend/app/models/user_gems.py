from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class UserGems(Base):
    __tablename__ = "user_gems"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    totalGemCount = Column(Float, default=0)
    highestTotalGems = Column(Float, default=0)
    availableGemsToMine = Column(Float, default=0)
    dailyGemsMined = Column(Float, default=0)
    mineTapLevel = Column(Integer, default=1)
    gemRechargeLevel = Column(Integer, default=1)

    user = relationship("User", back_populates="gems")