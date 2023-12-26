from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String(100), nullable=False)

class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    designation = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
    doj=Column(DateTime, nullable=False)


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    designation = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
    doj=Column(DateTime, nullable=False)

    manager_id = Column(Integer, ForeignKey("managers.id"))

