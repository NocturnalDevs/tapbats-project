# database/connection.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

print("Current Working Directory:", os.getcwd())

load_dotenv() 

DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL = "postgresql://username:password@localhost:5432/database" # use this and comment out line 13 if database connection is not working
print("DATABASE_URL:", DATABASE_URL)

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Create an engine to connect to the database
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
