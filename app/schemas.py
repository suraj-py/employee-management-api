from typing import Union, Optional, List
from pydantic import BaseModel
from datetime import date
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class DataToken(BaseModel):
    id: Optional[str] = None


class ManagerBase(BaseModel):
    company_id: int
    name: str
    email: str
    designation: str
    salary: float
    doj: date


class EmployeeBase(BaseModel):
    company_id: int
    name: str
    email: str
    designation: str
    salary: float
    doj: date

class Employee(EmployeeBase):
    id: int
    manager_id: Optional[int]
    class Config:
        orm_mode = True

class Manager(ManagerBase):
    id: int
    employees: List[Employee]=[]
    class Config:
        orm_mode = True
