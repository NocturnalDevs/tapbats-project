import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.models import Base, CavernTable, MinerTable, UserTable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import constants and data from constant_values.py
from constant_values import (
    caverns_data,
    miners_per_cavern,
    miner_stats,
)

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL = "postgresql://username:password@localhost:5432/database" # use this and comment out line 13 if database connection is not working
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to clear the database
def clear_database():
    print("Clearing the database...")
    Base.metadata.drop_all(bind=engine)  # Drop all tables
    Base.metadata.create_all(bind=engine)  # Recreate all tables
    print("Database cleared and recreated successfully!")

# Function to generate miner names
def generate_miner_names(cavern_name, count):
    base_name = cavern_name.split()[0]  # Use the first word of the cavern name
    return [f"{base_name} Miner {i+1}" for i in range(count)]

# Function to populate the tables
def populate_tables():
    db = SessionLocal()

    try:
        # Create a user with the specified values (DO NOT SET ID)
        user = UserTable(
            telegram_id="1928374650",
            username="GameMaster",
            referral_code="BAT219g",
        )
        db.add(user)
        db.commit()

        # Populate CavernTable
        for cavern_data in caverns_data:
            cavern = CavernTable(**cavern_data)
            db.add(cavern)
        db.commit()

        # Populate MinerTable
        for cavern_data in caverns_data:
            cavern_name = cavern_data["name"]
            cavern_id = db.query(CavernTable.id).filter(CavernTable.name == cavern_name).scalar()
            miner_count = miners_per_cavern[cavern_name]
            miner_names = generate_miner_names(cavern_name, miner_count)
            stats = miner_stats[cavern_name]

            for name in miner_names:
                miner = MinerTable(
                    name=name,
                    cavern_id=cavern_id,
                    cost=stats["cost"],
                    gems_per_hour=stats["gems_per_hour"],
                )
                db.add(miner)
        db.commit()

        print("Tables populated successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error populating tables: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    clear_database()  # Clear the database first
    populate_tables()  # Populate the tables