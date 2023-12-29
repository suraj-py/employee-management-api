from typing import Union, Optional, List
from pydantic import BaseModel, EmailStr
from datetime import date

# User's pydantic models or schemes
class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr]
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

# JWT pydantic models or schemes
class Token(BaseModel):
    access_token: str
    token_type: str

class DataToken(BaseModel):
    id: Optional[str] = None

# Employee's pydantic models or schemes
class EmployeeBase(BaseModel):
    company_id: int
    name: str
    email: EmailStr
    designation: str
    salary: float
    doj: date

class Employee(EmployeeBase):
    id: int
    manager_id: Optional[int]
    class Config:
        orm_mode = True

# Manager's pydantic models or schemes
class ManagerBase(BaseModel):
    company_id: int
    name: str
    email: EmailStr
    designation: str
    salary: float
    doj: date

class Manager(ManagerBase):
    id: int
    employees: List[Employee]=[]
    class Config:
        orm_mode = True
