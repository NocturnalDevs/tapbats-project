# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import SessionLocal, engine, get_db
from database.models import Base
from routers.user_router import router as user_router

# Create all tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Create a FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the user router
app.include_router(user_router, prefix="/api")