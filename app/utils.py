from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models, schemas, database
from dependencies import get_db

outh2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

SECRET_KEY = "75cd41725576d0a53ddf8d2c4b6daa3b0f35e5816b78c9a204368b752cf99e96"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encode_jwt

def verify_token_access(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.DataToken(id=id)
    except JWTError as e:
        print(e)
        raise credentials_exception

    return token_data

def get_current_user(token: str = Depends(outh2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not Validate Credentials",
                                headers={"WWW-Authenticate": "Bearer"})

    token = verify_token_access(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user


# create psasword context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# create hash password
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(non_hashed_pass, hashed_password):
    return pwd_context.verify(non_hashed_pass, hashed_password)


def create_user(db: Session, user: schemas.UserCreate):
    password = hash_password(user.password)
    db_user = models.User(username=user.username,
                        email=user.email,
                        hash_password=password
                    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_manager(db: Session, managers: schemas.ManagerBase):
    db_manager = models.Manager(**managers.dict())
    db.add(db_manager)
    db.commit()
    db.refresh(db_manager)
    return db_manager

def create_employees(db: Session, employees: schemas.EmployeeBase, manager_id: int):
    db_employee = models.Employee(**employees.dict(), manager_id=manager_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_managers_list(db: Session):
    return db.query(models.Manager).all()

def get_employees_list(db: Session):
    return db.query(models.Employee).all()
