from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models, schemas

# create psasword context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# create hash password
def hash_password(password: str):
    return pwd_context.hash(password)

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

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
