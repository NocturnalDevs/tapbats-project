from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class UserColonyMembers(Base):
    __tablename__ = "user_colony_members"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    memberName = Column(String)

    user = relationship("User", back_populates="colony_members")

class UserColonyElder(Base):
    __tablename__ = "user_colony_elder"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, ForeignKey("user.telegramID"))
    elderName = Column(String)

    user = relationship("User", back_populates="colony_elder")