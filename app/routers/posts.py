


from app.dependencies import Depends, HTTPException, Session, get_db, APIRouter

from app.db import crud, schemas
from app.security import oauth2_scheme


router = APIRouter(
    prefix="/api/v1",
    dependencies=[Depends(oauth2_scheme)],
    tags=["Post"],
)

#* Posts
@router.post("/createposts")
def post(user_id:int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    """Using this endpoint you can create a post """
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Username doesn't exist")  
    return  crud.create_post(db=db, post=post, user_id=user_id) 

@router.get("/allposts")
def all_posts(db: Session = Depends(get_db)):
    """Using this endpoint you can get all the posts from the DataBase """
    return  crud.get_posts(db=db) 
