

# fastapi imports
from fastapi import FastAPI
import uvicorn


# Local imports
from .db import models
from .db.database import engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI(redoc_url=None)


# Local Imports
from .utils import my_schema
app.openapi = my_schema 

#* ROUTES
from app.routers import users, posts, no_oauth

app.include_router(no_oauth.router)
app.include_router(users.router)
app.include_router(posts.router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)