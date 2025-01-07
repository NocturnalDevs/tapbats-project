from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import database
from app.api.endpoints import user, gems, quests, miners, caverns, story

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, prefix="/api/v1")
app.include_router(gems.router, prefix="/api/v1")
app.include_router(quests.router, prefix="/api/v1")
app.include_router(miners.router, prefix="/api/v1")
app.include_router(caverns.router, prefix="/api/v1")
app.include_router(story.router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()