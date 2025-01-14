from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal, engine
from database.models import Base
from routers.user_router import router as user_router

# Create all tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Create a FastAPI app instance
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include the user router
app.include_router(user_router, prefix="/api")