from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Quest(Base):
    __tablename__ = "quest"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # 'daily' or 'special'
    description = Column(String)
    rewardAmount = Column(Float)
    link = Column(String, nullable=True)
    requiredProgress = Column(Float, nullable=True)

class UserQuests(Base):
    __tablename__ = "user_quests"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    questID = Column(Integer, ForeignKey("quest.id"))
    currentProgress = Column(Float, default=0)
    completed = Column(Boolean, default=False)
    collected = Column(Boolean, default=False)
    due = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="quests")
    quest = relationship("Quest")