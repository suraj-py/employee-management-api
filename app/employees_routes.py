from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from app.database import SessionLocal, engine
from app.dependencies import get_db
from app.role_checker import RoleChecker
from app import schemas
from app import models
from app import curd

allow_create_read_resource = RoleChecker(["admin", "manager"])
allow_create_resource = RoleChecker(["admin", "manager", "employee"])

router = APIRouter(
    prefix="/companies",
    tags=["Employees"],
    dependencies = [Depends(allow_create_read_resource)],
    )

# create employee
@router.post("/employee", response_model=schemas.Employee)
async def create_employee(employee: schemas.EmployeeBase, manager_id: int, db: Session = Depends(get_db)):
    db_employee = curd.get_employees_by_company_id(db=db, company_id=employee.company_id)
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee already exists")
    return curd.create_employees(db=db, employees=employee, manager_id=manager_id)

# list all employee's
@router.get("/employees/all", response_model=List[schemas.Employee])
async def list_employees(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return curd.get_employee_list(db=db, skip=skip, limit=limit)

# list employee's by manager
@router.get("/employees/{company_id}/all", response_model=List[schemas.Employee])
async def list_employees_by_manager(manager_company_id: str, db: Session = Depends(get_db)):
    return curd.get_emp_list_by_manager(manager_company_id=manager_company_id, db=db)

# get details of single employee
@router.get("/employees/{company_id}", response_model=schemas.Employee, dependencies=[Depends(allow_create_resource)])
async def get_single_employee(company_id: str, db: Session = Depends(get_db)):
    single_employee = emp = curd.get_employees_by_company_id(db=db, company_id=company_id)
    return single_employee

# update employee details
@router.put("/employees/{company_id}/update")
async def update_employee(company_id:str, employee: schemas.EmployeeBase, db: Session = Depends(get_db)):
    emp = curd.get_employees_by_company_id(db=db, company_id=company_id)
    if not emp.first():
        raise HTTPException(status_code=404, detail='Employee not found')
    emp.update(employee.dict())
    db.commit()
    return {"Message":"Employee updated successfully"}

# delete employee
@router.delete("/employees/{company_id}/delete", dependencies=[Depends(allow_create_resource)])
async def delete_employee(company_id: str, db: Session = Depends(get_db)):
    emp = curd.delete_employee(db=db, company_id=company_id)
    return {"Message": "Employee deleted successfully"}



