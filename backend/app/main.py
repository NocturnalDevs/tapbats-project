from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine
from app.api.user import router as user_router
from app.api.user_gems import router as user_gems_router
from app.api.user_socials import router as user_socials_router
from app.api.user_colony import router as user_colony_router
from app.api.quest import router as quest_router
from app.api.miner import router as miner_router
from app.api.cavern import router as cavern_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/api")
app.include_router(user_gems_router, prefix="/api")
app.include_router(user_socials_router, prefix="/api")
app.include_router(user_colony_router, prefix="/api")
app.include_router(quest_router, prefix="/api")
app.include_router(miner_router, prefix="/api")
app.include_router(cavern_router, prefix="/api")
