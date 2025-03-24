from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from ..database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/productos/", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db=db, producto=producto)

@router.get("/productos/", response_model=list[schemas.Producto])
def read_productos(db: Session = Depends(get_db)):
    return crud.get_productos(db)

@router.get("/productos/{producto_id}", response_model=schemas.Producto)
def read_productobyid(producto_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.get_producto(db, producto_id=producto_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_cliente