import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.models import Base, CavernTable, MinerTable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://postgres:V8Bn1lv06lan90@localhost:5432/tapbats_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Data for CavernTable
caverns_data = [
    {"name": "Pebble Hollow", "cost": 0.0, "required_nocturnal_level": "Fledgling"},
    {"name": "Glimmer Grotto", "cost": 0.4, "required_nocturnal_level": "Warrior"},
    {"name": "Shimmerstone Den", "cost": 2.0, "required_nocturnal_level": "Shadow Warrior"},
    {"name": "Crystal Vein Hollow", "cost": 4.0, "required_nocturnal_level": "Eclipse Warrior"},
    {"name": "Prismstone Cavern", "cost": 20.0, "required_nocturnal_level": "Lunar Champion"},
    {"name": "Radiant Depths", "cost": 40.0, "required_nocturnal_level": "Nocturnal Beast"},
    {"name": "Emberglow Chasm", "cost": 80.0, "required_nocturnal_level": "Nightfall Guardian"},
    {"name": "Starfall Hollow", "cost": 200.0, "required_nocturnal_level": "Starlight Guardian"},
    {"name": "Obsidian Spire", "cost": 400.0, "required_nocturnal_level": "Eclipse Titan"},
    {"name": "Celestial Vault", "cost": 800.0, "required_nocturnal_level": "Shadow Lord"},
    {"name": "Eternal Lumina", "cost": 2000.0, "required_nocturnal_level": "Void Reaver"},
]

# Data for MinerTable
miners_per_cavern = {
    "Pebble Hollow": 10,
    "Glimmer Grotto": 10,
    "Shimmerstone Den": 10,
    "Crystal Vein Hollow": 10,
    "Prismstone Cavern": 8,
    "Radiant Depths": 8,
    "Emberglow Chasm": 8,
    "Starfall Hollow": 6,
    "Obsidian Spire": 6,
    "Celestial Vault": 6,
    "Eternal Lumina": 4,
}

miner_stats = {
    "Pebble Hollow": {"gems_per_hour": 20, "cost": 0.0001935},
    "Glimmer Grotto": {"gems_per_hour": 25, "cost": 0.000241875},
    "Shimmerstone Den": {"gems_per_hour": 30, "cost": 0.00029025},
    "Crystal Vein Hollow": {"gems_per_hour": 35, "cost": 0.000338625},
    "Prismstone Cavern": {"gems_per_hour": 50, "cost": 0.00048375},
    "Radiant Depths": {"gems_per_hour": 58, "cost": 0.00056115},
    "Emberglow Chasm": {"gems_per_hour": 65, "cost": 0.000628875},
    "Starfall Hollow": {"gems_per_hour": 98, "cost": 0.00094815},
    "Obsidian Spire": {"gems_per_hour": 105, "cost": 0.001015875},
    "Celestial Vault": {"gems_per_hour": 115, "cost": 0.001112625},
    "Eternal Lumina": {"gems_per_hour": 185, "cost": 0.001789875},
}

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

# Run the script
if __name__ == "__main__":
    populate_tables()