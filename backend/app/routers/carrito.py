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

@router.post("/carrito/", response_model=schemas.Carrito)
def create_carrito(carrito: schemas.CarritoCreate, db: Session = Depends(get_db)):
    return crud.create_carrito(db=db, carrito=carrito)

@router.get("/carrito/{carrito_id}", response_model=schemas.Cliente)
def read_carrito(carrito_id: int, db: Session = Depends(get_db)):
    db_carrito = crud.get_carrito(db, carrito_id=carrito_id)
    if db_carrito is None:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return db_carrito