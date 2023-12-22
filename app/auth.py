from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, models, utils
from database import SessionLocal, engine
from dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm

models.Base.metadata.create_all(bind=engine)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
    )


@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = utils.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return utils.create_user(db=db, user=user)

@router.post("/login", response_model=schemas.Token)
def login_user(userdetails: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = utils.get_user_by_username(db=db, username=userdetails.username)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='The User Does not exist')

    if not utils.verify_password(userdetails.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The Password do not match")

    access_token = utils.create_access_token(data={"user_id":user.id})

    return {"access_token":access_token, "token_type": "bearer"}
