


from app.dependencies import Depends, HTTPException, Session, get_db, APIRouter, status, OAuth2PasswordRequestForm
from app.db import crud, schemas
from app.security import oauth2_scheme

router = APIRouter()

@router.post("/register", response_model=schemas.User, tags=["Get Started"])
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """This endpoint is used to register Users to the DataBase."""
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username or email already taken")
    return crud.create_user(db=db, user=user)


@router.post("/token", tags=["Get Started"])
def get_bearer_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): 
    """Using this endpoint yo can get a bearer token you can use in your code, only fill in the username and password section"""
    
    user_dict = crud.get_user_by_username(db, form_data.username)

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    password = form_data.password
    if not password == user_dict.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user_dict.username, "token_type": "bearer"}