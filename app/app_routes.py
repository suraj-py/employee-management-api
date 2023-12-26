from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, models, utils
from database import SessionLocal, engine
from dependencies import get_db
from typing import List


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
