from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from .items import Item

# Definimos el modelo para un pedido
class Order(BaseModel):
    order_id: int
    customer_name: str
    items: List[Item]
    total: float

# Inicializamos el router para las rutas de pedidos
router = APIRouter()

# Lista de pedidos (deberías usar una base de datos real aquí)
orders_db = []

# Crear un nuevo pedido
@router.post("/orders/", response_model=Order)
async def create_order(order: Order):
    orders_db.append(order)
    return order

# Obtener todos los pedidos
@router.get("/orders/", response_model=List[Order])
async def get_orders():
    return orders_db

# Obtener un pedido por ID
@router.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    for order in orders_db:
        if order.order_id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")
