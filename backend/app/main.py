from fastapi import FastAPI
from app.routers import clientes, productos, carrito, tarjetas
from app.database import Base, engine

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(carrito.router)
app.include_router(tarjetas.router)