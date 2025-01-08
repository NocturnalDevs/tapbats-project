from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    telegramID = Column(String, unique=True, index=True)
    telegramName = Column(String, nullable=False)
    lastOnline = Column(DateTime, nullable=True)
    referralCode = Column(String, unique=True)

    # Relationships
    gems = relationship("UserGems", back_populates="user")
    socials = relationship("UserSocials", back_populates="user")
    colony_members = relationship("UserColonyMembers", back_populates="user")
    colony_elder = relationship("UserColonyElder", back_populates="user")
    quests = relationship("UserQuests", back_populates="user")
    miners = relationship("UserMiners", back_populates="user")
    caverns = relationship("UserCaverns", back_populates="user")