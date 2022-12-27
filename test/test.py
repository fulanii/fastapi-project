

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_ex = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "secret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "password": "secret2",
        "disabled": False,
    },
}

def get_current_user(token_username: str = Depends(oauth2_scheme)):
    user = user_ex[token_username]
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@app.post("/token")
def get_bearer_token(form_data: OAuth2PasswordRequestForm = Depends()): 
    """Using this endpoint yo can get a bearer toekn you can use in your code, only fill in the username and password section"""
    user_dict = user_ex.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    password = form_data.password
    if not password == user_dict["password"]:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user_dict["username"], "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(current_user = Depends(get_current_user)):
    return current_user

@app.get("/hey")
def say_hello(token_username:str = Depends(oauth2_scheme)):
    return {"hello": token_username}

import requests

