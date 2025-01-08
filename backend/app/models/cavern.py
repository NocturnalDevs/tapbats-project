from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Cavern(Base):
    __tablename__ = "cavern"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    requiredProgress = Column(Float)

class UserCaverns(Base):
    __tablename__ = "user_caverns"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    cavernID = Column(Integer, ForeignKey("cavern.id"))
    owned = Column(Boolean, default=False)
    currentProgress = Column(Float, default=0)

    user = relationship("User", back_populates="caverns")
    cavern = relationship("Cavern")