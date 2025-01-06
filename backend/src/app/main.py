from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import database
from app.schemas import user
from app.api.endpoints import user as user_endpoints

app = FastAPI()

# Include routers
app.include_router(user_endpoints.router, prefix="/api/v1")

# Dependency to get the database session
@app.on_event("startup")
async def startup():
    from app.database.database import Base, engine
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    pass