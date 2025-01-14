# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal, engine, get_db
from database.models import Base
from routers.user_router import router as user_router

# Create all tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Create a FastAPI app instance
app = FastAPI()

# Include the user router
app.include_router(user_router, prefix="/api")