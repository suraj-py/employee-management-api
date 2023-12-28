from passlib.context import CryptContext

# create psasword context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# create hash password
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(non_hashed_pass, hashed_password):
    return pwd_context.verify(non_hashed_pass, hashed_password)


