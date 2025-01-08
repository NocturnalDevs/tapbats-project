from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Import all models to ensure they are registered with SQLAlchemy
from app.models.user import User
from app.models.user_gems import UserGems
from app.models.user_socials import UserSocials
from app.models.user_colony import UserColonyMembers, UserColonyElder
from app.models.quest import Quest, UserQuests
from app.models.miner import Miner, UserMiners
from app.models.cavern import Cavern, UserCaverns

# Create all tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()