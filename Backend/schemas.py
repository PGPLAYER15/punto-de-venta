from pydantic import BaseModel
from typing import List, Optional

# Esquema para creación de usuario (POST)
class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    password: str

# Esquema para respuesta de usuario (GET)
class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str

    class Config:
        orm_mode = True  # Permite usar ORM de SQLAlchemy


class ItemCarritoBase(BaseModel):
    producto_id: int
    cantidad: int = 1

class ItemCarritoCreate(ItemCarritoBase):
    pass

class ItemCarritoResponse(ItemCarritoBase):
    id: int
    producto: dict  # Usará el esquema de respuesta de Producto

    class Config:
        orm_mode = True

class CarritoResponse(BaseModel):
    id: int
    usuario_id: int
    items: List[ItemCarritoResponse]

    class Config:
        orm_mode = True
