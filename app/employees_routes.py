from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from database import SessionLocal, engine
from dependencies import get_db
import schemas, models, curd

router = APIRouter(
    prefix="/employee",
    tags=["Employees"]
    )

@router.post("/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeBase, manager_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.company_id == employee.company_id).first()
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee alreadt exists")
    return curd.create_employees(db=db, employees=employee, manager_id=manager_id)

@router.put("/{employee_id}")
def update_employee(employee_id:int, employee: schemas.EmployeeBase, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id)
    if not emp.first():
        raise HTTPException(status_code=404, detail='Employee not found')
    emp.update(employee.dict())
    db.commit()
    return {"Message":"Employee updated successfully"}

@router.get("/{employee_id}", response_model=schemas.Employee)
def get_single_employee(company_id: int, db: Session = Depends(get_db)):
    single_employee = db.query(models.Employee).filter(models.Employee.company_id == company_id).first()
    return single_employee

@router.delete("/delete")
def delete_employee(company_id: int, db: Session = Depends(get_db)):
    emp = curd.delete_employee(db=db, company_id=company_id)
    return {"Message": "Employee deleted successfully"}



