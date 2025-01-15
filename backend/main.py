from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import SessionLocal, engine, get_db
from database.models import Base
from routers.user_router import router as user_router

# Create all tables (if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.options("/api/test-cors")
async def test_cors():
    return {"message": "CORS preflight handled"}

@app.get("/api/test-cors")
async def test_cors_get():
    return {"message": "CORS GET request handled"}

app.include_router(user_router, prefix="/api")