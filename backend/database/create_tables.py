from connection import engine, Base
from models import (
    UserTable, UserFundsTable, UserTapMiningTable, CavernTable, MinerTable,
    UserCavernTable, UserMinerTable, UserSocialsTable, QuestTable,
    UserQuestTable, UserElderTable, UserMembersTable
)

# Enable detailed logging
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")