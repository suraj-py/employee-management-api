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

allow_create_resource = RoleChecker(["admin", "manager"])
allow_create_read_resource = RoleChecker(["admin"])

router = APIRouter(
    prefix="/companies",
    tags=["Managers"],
    dependencies=[Depends(allow_create_resource)],
    )

# create manager
@router.post("/manager", response_model=schemas.Manager, dependencies=[Depends(allow_create_read_resource)])
async def create_manager(manager: schemas.ManagerBase, db: Session = Depends(get_db)):
    db_manager = db.query(models.Manager).filter(models.Manager.company_id == manager.company_id).first()
    if db_manager:
        raise HTTPException(status_code=400, detail="Manager already exists")
    return curd.create_manager(db=db, managers=manager)

# list all managers
@router.get("/managers/all", response_model=List[schemas.Manager], dependencies=[Depends(allow_create_read_resource)])
async def list_managers(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return curd.get_managers_list(db=db, skip=skip, limit=limit)

# get details of single manager
@router.get("/managers/{company_id}", response_model=schemas.Manager)
async def single_manager(company_id: str, db: Session = Depends(get_db)):
    return curd.get_manager_by_company_id(db=db, company_id=company_id)

# update manager
@router.put("/managers/{manager_id}/update")
async def update_manager(manager_id:int, manager: schemas.ManagerBase, db: Session = Depends(get_db)):
    mng = db.query(models.Manager).filter(models.Manager.id == manager_id)
    if not mng.first():
        raise HTTPException(status_code=404, detail='Employee not found')
    mng.update(manager.dict())
    db.commit()
    return {"Message":"Employee updated successfully"}

# delete manager
@router.delete("/managers/{company_id}/delete")
async def delete_manager(company_id: str, db: Session = Depends(get_db)):
    emp = curd.delete_manager(db=db, company_id=company_id)
    return {"Message": "Manager deleted successfully"}

