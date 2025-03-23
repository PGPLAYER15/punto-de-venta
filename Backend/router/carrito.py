from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/carrito", tags=["Carrito"])

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/", response_model=schemas.ItemCarritoResponse)
async def agregar_item(item: schemas.ItemCarritoCreate, db: Session = Depends(get_db)):
    # Verificar si el producto existe
    db_producto = db.query(models.Producto).filter(models.Producto.id == item.producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Crear nuevo item en el carrito (ejemplo: usuario fijo, en producción usar autenticación)
    db_item = models.ItemCarrito(**item.dict(), carrito_id=1)  # Cambiar "1" por el ID del carrito del usuario autenticado
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=schemas.CarritoResponse)
async def ver_carrito(db: Session = Depends(get_db)):
    carrito = db.query(models.Carrito).filter(models.Carrito.id == 1).first()  # Ejemplo con carrito ID 1
    if not carrito:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return carrito
