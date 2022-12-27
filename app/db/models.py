

from app.dependencies import Boolean, Column, ForeignKey, Integer, String, relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)

    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String , nullable=False)

    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)


    owner_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    owner = relationship("User", back_populates="posts")

