from fastapi import FastAPI
from database import engine
from typing import Union
import models  # Importación directa
from ..Routes import items, orders, payments, users, carrito

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir los routers en la aplicación principal
app.include_router(items.router, prefix="/api")
app.include_router(orders.router, prefix="/api")
app.include_router(payments.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(carrito.router, prefix="/api")

# Ruta de prueba
@app.get("/")
async def read_root():
    return {"message": "Bienvenido al sistema de punto de venta"}
