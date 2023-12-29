from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import List

from database import SessionLocal, engine
from dependencies import get_db
from role_checker import RoleChecker
import schemas, models, curd

allow_create_resource = RoleChecker(["admin", "manager"])
allow_create_read_resource = RoleChecker(["admin"])

router = APIRouter(
    prefix="/manager",
    tags=["Managers"]
    )

@router.post("/", response_model=schemas.Manager, dependencies=[Depends(allow_create_read_resource)])
def create_manager(manager: schemas.ManagerBase, db: Session = Depends(get_db)):
    db_manager = db.query(models.Manager).filter(models.Manager.company_id == manager.company_id).first()
    if db_manager:
        raise HTTPException(status_code=400, detail="Manager alreadt exists")
    return curd.create_manager(db=db, managers=manager)

@router.get("/all_managers", response_model=List[schemas.Manager], dependencies=[Depends(allow_create_read_resource)])
def list_managers(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return curd.get_managers_list(db=db, skip=skip, limit=limit)

@router.get("/{company_id}", response_model=schemas.Manager, dependencies=[Depends(allow_create_resource)])
def single_manager(company_id: int, db: Session = Depends(get_db)):
    return curd.get_manager_by_company_id(db=db, company_id=company_id)

@router.put("/{manager_id}", dependencies=[Depends(allow_create_resource)])
def update_manager(manager_id:int, manager: schemas.ManagerBase, db: Session = Depends(get_db)):
    mng = db.query(models.Manager).filter(models.Manager.id == manager_id)
    if not mng.first():
        raise HTTPException(status_code=404, detail='Employee not found')
    mng.update(manager.dict())
    db.commit()
    return {"Message":"Employee updated successfully"}

@router.delete("/delete", dependencies=[Depends(allow_create_resource)])
def delete_manager(company_id: int, db: Session = Depends(get_db)):
    emp = curd.delete_manager(db=db, company_id=company_id)
    return {"Message": "Manager deleted successfully"}
