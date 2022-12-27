

from app.dependencies import BaseModel


class PostBase(BaseModel):
    """Base Models with all attributes needed when reading/creating data"""
    title: str
    description: str

class PostCreate(PostBase):
    """Create Models Inherit from Base here put all (attributes) needed for creation. Ex: here none since everything needed for creation is alredy being inherited from the Base Model"""
    pass

class Post(PostCreate):
    """
    This model (schemas) is used when reading data (returning it from the api), 
    So when we make an api call to get post or posts we get: post_id, title and description 
    """
    post_id: int
    title: str
    description: str

    class Config:
        """
        orm_mode = True. Tells Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).

        This way, instead of only trying to get the id value from a dict, as in: 
        id = data["id"]

        it will also try to get it from an attribute, as in:
        id = data.it
        """
        orm_mode = True

#****************
#****************

class UserBase(BaseModel): 
    """Base Models with all attributes needed when reading/creating data"""
    email: str
    name: str
    username: str

class UserCreate(UserBase): 
    """Create Models Inherit from Base here put all (attributes) needed for creation. Ex: here password is needed when creating this User Model"""
    password: str

class User(UserBase):
    """
    This model (schemas) is used when reading data (returning it from the api), So when we make an api call to get a user or users we get:
    user_id, email, name, username, is_active and posts(user made), (Notice we dont return password here)
    """
    user_id: int
    email: str
    name: str
    username: str
    is_active: bool
    posts: list[Post] = []

    class Config:
        """
        orm_mode = True. Tells Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).

        This way, instead of only trying to get the id value from a dict, as in: 
        id = data["id"]

        it will also try to get it from an attribute, as in:
        id = data.it
        """
        orm_mode = True






