from ..database import crud, models, database

def check_user_exist(telegramID: str, db: Session):
    return crud.get_user(db, telegramID=telegramID)

def create_user(telegramID: str, db: Session):
    return crud.create_user(db, telegramID=telegramID)