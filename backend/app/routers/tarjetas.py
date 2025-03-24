from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tarjetas/", response_model=schemas.Tarjeta)
def create_tarjeta(tarjeta: schemas.TarjetaCreate, db: Session = Depends(get_db)):
    return crud.create_tarjeta(db=db, tarjeta=tarjeta)

@router.get("/tarjetas/{tarjetas_id}", response_model=schemas.Tarjeta)
def read_tarjeta(tarjetas_id: int, db: Session = Depends(get_db)):
    db_tarjeta = crud.get_tarjeta(db, tarjetas_id=tarjetas_id)
    if db_tarjeta is None:
        raise HTTPException(status_code=404, detail="Tarjeta no encontrado")
    return db_tarjeta