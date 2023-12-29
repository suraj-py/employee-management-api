from passlib.context import CryptContext
import random
# create psasword context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# create hash password
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(non_hashed_pass, hashed_password):
    return pwd_context.verify(non_hashed_pass, hashed_password)

# create company id
nums = '1234567890'
def generate_company_id(role):
    # role = M for Manager and
    # role = E for Employee
    id = []
    for i in range(4):
        id.append(random.choice(nums))
    return role + ''.join(id)


