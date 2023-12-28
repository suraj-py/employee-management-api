from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import SessionLocal, engine
from dependencies import get_db
from curd import create_user, get_user_by_username, get_user_by_email
from utils import verify_password
from oauth2 import create_access_token
import schemas, models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="",
    tags=["Authentication"]
    )

@router.post("/admin/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.post("/login", response_model=schemas.Token)
def login_user(userdetails: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db=db, username=userdetails.username)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='The User Does not exist')

    if not verify_password(userdetails.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The Password do not match")

    access_token = create_access_token(data={"user_id":user.id})

    return {"access_token":access_token, "token_type": "bearer"}

