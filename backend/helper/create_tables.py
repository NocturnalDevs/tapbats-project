# backend/create_tables.py

from backend.database.connection import engine, Base
from backend.database.models import User  # Import your models here

def create_tables():
    """
    Create all tables in the database based on the SQLAlchemy models.
    """
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()