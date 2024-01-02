from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import SessionLocal, engine
from app.dependencies import get_db
from app.curd import create_user, get_user_by_username, get_user_by_email
from app.utils import verify_password
from app.oauth2 import create_access_token, outh2_scheme, get_current_user
from app.role_checker import RoleChecker
from app import schemas
from app import models

models.Base.metadata.create_all(bind=engine)

allow_create_resource = RoleChecker(["admin"])

router = APIRouter(
    prefix="/company",
    tags=["Authentication"],
    )

# create a new user
@router.post("/register", response_model=schemas.User)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

# login function
@router.post("/login", response_model=schemas.Token)
async def login_user(userdetails: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db=db, username=userdetails.username)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='The User Does not exist')

    if not verify_password(userdetails.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The Password do not match")

    access_token = create_access_token(data={"user_id":user.id})

    return {"access_token":access_token, "token_type": "bearer"}


@router.get("/user")
async def user(user: schemas.UserBase = Depends(get_current_user)):
    return user
