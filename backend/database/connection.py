# database/connection.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging

print("Current Working Directory:", os.getcwd())

load_dotenv() 

# Enable detailed logging
logger = logging.getLogger(__name__)

# Load DATABASE_URL from environment variable
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://postgres:V8Bn1lv06lan90@localhost:5432/tapbats_db" # change this to point towards your postgresql database
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

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)