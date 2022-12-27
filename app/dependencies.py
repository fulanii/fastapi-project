

from fastapi import APIRouter, Depends, HTTPException, status, Security
from pydantic import BaseModel
from fastapi.security.api_key import APIKeyHeader, APIKey
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from starlette.status import HTTP_403_FORBIDDEN
from typing import Set, Union

from .db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



