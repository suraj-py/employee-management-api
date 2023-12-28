from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_db
import models, schemas

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

def delete_employee(db: Session, company_id: int):
    emp = db.query(models.Employee).filter(models.Employee.company_id == company_id).delete()
    db.commit()
    return emp

def delete_manager(db: Session, company_id: int):
    emp = db.query(models.Manager).filter(models.Manager.company_id == company_id).delete()
    db.commit()
    return emp
