from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from database import SessionLocal, engine
from dependencies import get_db
from role_checker import RoleChecker
import schemas, models, curd


allow_create_read_resource = RoleChecker(["admin", "manager"])
allow_create_resource = RoleChecker(["admin", "manager", "employee"])

router = APIRouter(
    prefix="/employee",
    tags=["Employees"],
    dependencies = [Depends(allow_create_read_resource)],
    )

@router.post("/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeBase, manager_id: int, db: Session = Depends(get_db)):
    db_employee = curd.get_employees_by_company_id(db=db, company_id=employee.company_id)
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee already exists")
    return curd.create_employees(db=db, employees=employee, manager_id=manager_id)

@router.get("/all_employees", response_model=List[schemas.Employee])
def list_employees(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return curd.get_employee_list(db=db, skip=skip, limit=limit)

@router.get("/all_employees_by_manager", response_model=List[schemas.Employee])
def list_employees_by_manager(manager_company_id: str, db: Session = Depends(get_db)):
    return curd.get_emp_list_by_manager(manager_company_id=manager_company_id, db=db)

@router.put("/{company_id}")
def update_employee(company_id:str, employee: schemas.EmployeeBase, db: Session = Depends(get_db)):
    emp = curd.get_employees_by_company_id(db=db, company_id=company_id)
    if not emp.first():
        raise HTTPException(status_code=404, detail='Employee not found')
    emp.update(employee.dict())
    db.commit()
    return {"Message":"Employee updated successfully"}

@router.get("/{company_id}", response_model=schemas.Employee, dependencies=[Depends(allow_create_resource)])
def get_single_employee(company_id: str, db: Session = Depends(get_db)):
    single_employee = emp = curd.get_employees_by_company_id(db=db, company_id=company_id)
    return single_employee

@router.delete("/delete", dependencies=[Depends(allow_create_resource)])
def delete_employee(company_id: str, db: Session = Depends(get_db)):
    emp = curd.delete_employee(db=db, company_id=company_id)
    return {"Message": "Employee deleted successfully"}



