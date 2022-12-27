
from .main import app
from fastapi.openapi.utils import get_openapi


def my_schema():
   openapi_schema = get_openapi(
       title="The Amazing Programming Language Info API",
       version="1.0",
       routes= app.routes, #routes
   )
   openapi_schema["info"] = {
       "title" : "Yassine Rest API project with FastAPI",
       "version" : "1.0",
       "description" : "This API project is a social medial style api, where users can regiter, get authenticate, post, see post etc..",
       "contact": {
           "name": "Get Help with this API",
           "url": "http://www.github.com/fulanii"
       }
   }
   app.openapi_schema = openapi_schema
   
   return app.openapi_schema
