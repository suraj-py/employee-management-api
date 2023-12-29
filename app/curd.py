from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_db
from utils import hash_password
import models, schemas

# util functions for users
# create user
def create_user(db: Session, user: schemas.UserCreate):
    password = hash_password(user.password)
    db_user = models.User(username=user.username,
                        email=user.email,
                        role=user.role,
                        hash_password=password
                    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# get user details by username
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# get user details by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# util functions for managers
# create manager
def create_manager(db: Session, managers: schemas.ManagerBase):
    db_manager = models.Manager(**managers.dict())
    db.add(db_manager)
    db.commit()
    db.refresh(db_manager)
    return db_manager

# get list of all managers
def get_managers_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Manager).offset(skip).limit(limit).all()

# get employee by company
def get_manager_by_company_id(db: Session, company_id: str):
    return db.query(models.Manager).filter(models.Manager.company_id == company_id).first()

# delete manager by company id
def delete_manager(db: Session, company_id: str):
    emp = db.query(models.Manager).filter(models.Manager.company_id == company_id).delete()
    db.commit()
    return emp

# util functions for employees
# create employee
def create_employees(db: Session, employees: schemas.EmployeeBase, manager_id: int):
    db_employee = models.Employee(**employees.dict(), manager_id=manager_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# get list of all employees
def get_employee_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

# get employees list by manager name
def get_emp_list_by_manager(manager_company_id: int, db: Session):
    manager = db.query(models.Manager).filter(models.Manager.company_id == manager_company_id).first()
    if manager:
        return manager.employees
    return {"Message":"Invalid manager company id"}

# get employee by company
def get_employees_by_company_id(db: Session, company_id: int):
    return db.query(models.Employee).filter(models.Employee.company_id == company_id).first()

# delete employee by company_id
def delete_employee(db: Session, company_id: int):
    emp = db.query(models.Employee).filter(models.Employee.company_id == company_id).delete()
    db.commit()
    return emp

