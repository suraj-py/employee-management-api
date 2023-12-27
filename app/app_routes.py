from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, models, utils
from database import SessionLocal, engine
from dependencies import get_db
from typing import List
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/app_routes",
    tags=["App Routes"]
    )

@router.post("/manager", response_model=schemas.Manager)
def create_manager(manager: schemas.ManagerBase, db: Session = Depends(get_db)):
    db_manager = db.query(models.Manager).filter(models.Manager.company_id == manager.company_id).first()
    if db_manager:
        raise HTTPException(status_code=400, detail="Manager alreadt exists")
    return utils.create_manager(db=db, managers=manager)

@router.get("/managers_list", response_model=List[schemas.Manager])
def list_managers(db: Session = Depends(get_db)):
    return utils.get_managers_list(db)


@router.post("/{manager_id}/employee", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeBase, manager_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.company_id == employee.company_id).first()
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee alreadt exists")
    return utils.create_employees(db=db, employees=employee, manager_id=manager_id)

@router.get("/employee/{employee_id}", response_model=schemas.Employee)
def get_single_employee(employee_id: int, db: Session = Depends(get_db)):
    single_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if single_employee:
        return single_employee
