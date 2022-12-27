

# Note: CRUD comes from: Create, Read, Update, and Delete.

from app.dependencies import Session

from . import models, schemas


#** User

def create_user(db: Session, user: schemas.UserCreate):
    """This methed creates users and add then to the DataBase 
    Data needed (email, name, username and password)
    """
    haspassword= user.password # come backa nd hash password latter
    db_user = models.User(email=user.email, name=user.name, username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id:int):
    """This function returns 1 specific user from DataBase using their user id."""
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username:str):
    """This function returns 1 specify user from the DataBase using the provided user: username."""
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email:str):
    """This function returns 1 specify user from the DataBase using the provided user: email."""
    return db.query(models.User).filter(models.User.email == email).first()

def get_all_users(db: Session, limit: int = 5):
    """This functions returns all users from the database, limit by default is 5."""
    return db.query(models.User).limit(limit).all()

#*** POST

def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    """This method creates posts using a user user_id and add them to the DataBase."""
    db_post = models.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session):
    """This method returns all posts """
    return db.query(models.Post).all()


