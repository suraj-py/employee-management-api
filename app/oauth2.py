from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from jose import JWTError, jwt
from datetime import timedelta, datetime
from dotenv import load_dotenv
import os

from dependencies import get_db
import models, schemas

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
outh2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

SECRET_KEY = secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# create jwt access token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encode_jwt

# verifing access token
def verify_token_access(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.DataToken(id=id)

    except JWTError:
        raise credentials_exception

    return token_data

# get current user
def get_current_user(token: str = Depends(outh2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not Validate Credentials",
                                headers={"WWW-Authenticate": "Bearer"})

    token = verify_token_access(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user

def get_current_user_role(playload: str = Depends(get_current_user)):
    print(playload)
