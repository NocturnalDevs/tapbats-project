import sys
import os
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import models and CRUD functions
from app.database import models, crud
from app.database.database import Base, SessionLocal, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

# Helper function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test User CRUD Operations
def test_user_crud(db: Session):
    print("Testing User CRUD Operations...")

    # Create a new user
    telegramID = "test_user_123"
    user = crud.create_user(db, telegramID)
    print(f"Created User: {user.telegramID}")

    # Get the user
    fetched_user = crud.get_user(db, telegramID)
    print(f"Fetched User: {fetched_user.telegramID}")

    # Update the user's last online timestamp
    lastOnline = datetime.now()
    updated_user = crud.update_user_last_online(db, telegramID, lastOnline)
    print(f"Updated User Last Online: {updated_user.lastOnline}")

    print("User CRUD Tests Passed!\n")

# Test UserGems CRUD Operations
def test_user_gems_crud(db: Session):
    print("Testing UserGems CRUD Operations...")

    # Create a new user
    telegramID = "test_user_123"
    user = crud.create_user(db, telegramID)

    # Create user gems
    gems = crud.create_user_gems(db, telegramID)
    print(f"Created User Gems: {gems.telegramID}")

    # Update user gems
    updated_gems = crud.update_user_gems(db, telegramID, totalGemCount=100, availableGemsToMine=50, dailyGemsMined=10)
    print(f"Updated User Gems - Total Gems: {updated_gems.totalGemCount}, Available Gems: {updated_gems.availableGemsToMine}, Daily Gems: {updated_gems.dailyGemsMined}")

    # Update highest total gems
    updated_highest_gems = crud.update_highest_total_gems(db, telegramID, highestTotalGems=100)
    print(f"Updated Highest Total Gems: {updated_highest_gems.highestTotalGems}")

    print("UserGems CRUD Tests Passed!\n")

# Test UserSocials CRUD Operations
def test_user_socials_crud(db: Session):
    print("Testing UserSocials CRUD Operations...")

    # Create a new user
    telegramID = "test_user_123"
    user = crud.create_user(db, telegramID)

    # Create user socials
    socials = crud.create_user_socials(db, telegramID)
    print(f"Created User Socials: {socials.telegramID}")

    # Update user socials
    updated_socials = crud.update_user_socials(db, telegramID, platform="youtube", username="test_youtube", verified=True)
    print(f"Updated User Socials - YouTube: {updated_socials.youtubeUsername}, Verified: {updated_socials.youtubeVerified}")

    print("UserSocials CRUD Tests Passed!\n")

# Test UserColony CRUD Operations
def test_user_colony_crud(db: Session):
    print("Testing UserColony CRUD Operations...")

    # Create a new user
    telegramID = "test_user_123"
    user = crud.create_user(db, telegramID)

    # Add a colony member
    member = crud.add_user_colony_member(db, telegramID, memberName="Test Member")
    print(f"Added Colony Member: {member.memberName}")

    # Set colony elder
    elder = crud.set_user_colony_elder(db, telegramID, elderName="Test Elder")
    print(f"Set Colony Elder: {elder.elderName}")

    print("UserColony CRUD Tests Passed!\n")

# Test Quest CRUD Operations
def test_quest_crud(db: Session):
    print("Testing Quest CRUD Operations...")

    # Create a new quest
    quest = models.Quest(
        type="daily",
        description="Mine 10 gems",
        rewardAmount=10,
        requiredProgress=10
    )
    db.add(quest)
    db.commit()
    db.refresh(quest)
    print(f"Created Quest: {quest.description}")

    # Create a new user
    telegramID = "test_user_123"
    user = crud.create_user(db, telegramID)

    # Create user quest
    user_quest = crud.create_user_quest(db, telegramID, quest.id)
    print(f"Created User Quest: {user_quest.questID}")

    # Update user quest progress
    updated_quest = crud.update_user_quest_progress(db, telegramID, quest.id, currentProgress=5)
    print(f"Updated User Quest Progress: {updated_quest.currentProgress}")

    # Mark quest as collected
    collected_quest = crud.mark_user_quest_collected(db, telegramID, quest.id)
    print(f"Marked Quest as Collected: {collected_quest.collected}")

    print("Quest CRUD Tests Passed!\n")

# Test Miner CRUD Operations
def test_miner_crud(db: Session):
    print("Testing Miner CRUD Operations...")

    # Create a new miner
    miner = models.Miner(
        name="Test Miner",
        description="A test miner",
        mineAmountPerSec=1,
        levelUpGemRequirement=100,
        requiredProgress=50
    )
    db.add(miner)
    db.commit()
    db.refresh(miner)
    print(f"Created Miner: {miner.name}")

    # Create a new user
    telegramID = "test_user_123"
    user = crud.create_user(db, telegramID)

    # Create user miner
    user_miner = crud.create_user_miner(db, telegramID, miner.id)
    print(f"Created User Miner: {user_miner.minerID}")

    # Update user miner progress
    updated_miner = crud.update_user_miner_progress(db, telegramID, miner.id, currentProgress=25)
    print(f"Updated User Miner Progress: {updated_miner.currentProgress}")

    print("Miner CRUD Tests Passed!\n")

# Test Cavern CRUD Operations
def test_cavern_crud(db: Session):
    print("Testing Cavern CRUD Operations...")

    # Create a new cavern
    cavern = models.Cavern(
        name="Test Cavern",
        description="A test cavern",
        requiredProgress=100
    )
    db.add(cavern)
    db.commit()
    db.refresh(cavern)
    print(f"Created Cavern: {cavern.name}")

    # Create a new user
    telegramID = "test_user_123"
    user = crud.create_user(db, telegramID)

    # Create user cavern
    user_cavern = crud.create_user_cavern(db, telegramID, cavern.id)
    print(f"Created User Cavern: {user_cavern.cavernID}")

    # Update user cavern progress
    updated_cavern = crud.update_user_cavern_progress(db, telegramID, cavern.id, currentProgress=50)
    print(f"Updated User Cavern Progress: {updated_cavern.currentProgress}")

    print("Cavern CRUD Tests Passed!\n")

# Test StoryPage CRUD Operations
def test_story_page_crud(db: Session):
    print("Testing StoryPage CRUD Operations...")

    # Create a new story page
    story_page = models.StoryPage(
        pageNumber=1,
        URL="https://example.com/story1.jpg",
        requiredGems=100
    )
    db.add(story_page)
    db.commit()
    db.refresh(story_page)
    print(f"Created Story Page: {story_page.pageNumber}")

    # Get unlocked story pages
    unlocked_pages = crud.get_unlocked_story_pages(db, highestTotalGems=150)
    print(f"Unlocked Story Pages: {[page.pageNumber for page in unlocked_pages]}")

    print("StoryPage CRUD Tests Passed!\n")

# Main function to run all tests
def main():
    db = SessionLocal()

    try:
        test_user_crud(db)
        test_user_gems_crud(db)
        test_user_socials_crud(db)
        test_user_colony_crud(db)
        test_quest_crud(db)
        test_miner_crud(db)
        test_cavern_crud(db)
        test_story_page_crud(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()