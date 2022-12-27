

from app.dependencies import Depends, HTTPException, Session, get_db, APIKey, APIRouter, status, OAuth2PasswordRequestForm
from app.db import crud, schemas

from app.db import crud, schemas
from app.security import oauth2_scheme


router = APIRouter(
    prefix="/api/v1",
    dependencies=[Depends(oauth2_scheme)],
    tags=["User"]
)


@router.get("/username", response_model=schemas.User)
def username(username: str, db: Session = Depends(get_db)):
    """This endpoint returns a specific user from the DataBase using their username"""
    db_user = crud.get_user_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Username not found")
    return db_user

@router.get("/email", response_model=schemas.User)
def email(email: str, db: Session = Depends(get_db)):
    """This endpoint returns a specific user from the DataBase using their email"""
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Email not found")
    return db_user  

@router.get("/allusers", response_model=list[schemas.User])
def users(limit: int = 5, db: Session = Depends(get_db)):
    """This endpoint return a list of users from the DataBase the default limit is 5"""
    users = crud.get_all_users(db=db, limit=limit)
    return users

@router.get("/myinfo", response_model=schemas.User)
def my_info(username:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Use this endpoint to get all your info while login"""
    my_info = crud.get_user_by_username(username=username, db=db)
    return my_info