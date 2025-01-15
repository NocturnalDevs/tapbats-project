from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import SessionLocal, engine, get_db
from database.models import Base
from routers.user_router import router as user_router
import uvicorn
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to terminal
    ],
)
logger = logging.getLogger(__name__)

# Create all tables (if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Update CORS middleware to allow your frontend's origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Local development
        "https://6b15-136-158-103-116.ngrok-free.app",  # Your ngrok URL / frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(user_router, prefix="/api")

@app.get("/")
def read_root():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug",
    )