import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.models import Base, CavernTable, MinerTable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import constants and data from constant_values.py
from constant_values import (
    caverns_data,
    miners_per_cavern,
    miner_stats,
)

# Database connection
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://postgres:V8Bn1lv06lan90@localhost:5432/tapbats_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Function to generate miner names
def generate_miner_names(cavern_name, count):
    base_name = cavern_name.split()[0]  # Use the first word of the cavern name
    return [f"{base_name} Miner {i+1}" for i in range(count)]

# Function to populate the tables
def populate_tables():
    db = SessionLocal()

    try:
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
    populate_tables()