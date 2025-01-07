# this will create all tables on Postgresql based on the models.py

from app.database.database import Base, engine

# Recreate all tables
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
