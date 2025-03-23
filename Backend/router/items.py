from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Definimos el modelo para un artículo
class Item(BaseModel):
    item_id: int
    name: str
    description: str
    price: float

router = APIRouter()

# Usar base de datos real en lugar de lista en memoria
@router.post("/items/")
async def create_item(nombre: str, precio: float):
    db = SessionLocal()
    try:
        new_product = Producto(nombre=nombre, precio=precio, stock=0)
        db.add(new_product)
        db.commit()
        return {"message": "Producto creado"}
    finally:
        db.close()

# Obtener todos los artículos
@router.get("/items/", response_model=List[Item])
async def get_items():
    return items_db

# Obtener un artículo por ID
@router.get("/items/{item_id}", response_model=Item)
async def get_itembyid(item_id: int):
    for item in items_db:
        if item.item_id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Actualizar un artículo por ID
@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    for idx, existing_item in enumerate(items_db):
        if existing_item.item_id == item_id:
            items_db[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Eliminar un artículo por ID
@router.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.item_id == item_id:
            deleted_item = items_db.pop(idx)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")
