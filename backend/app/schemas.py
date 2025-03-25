from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    email: str

class ClienteCreate(ClienteBase):
    password: str

class ClienteUpdate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True

class ProductoUpdate(ProductoBase):
    pass

class CarritoBase(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int

class CarritoCreate(CarritoBase):
    pass

class Carrito(CarritoBase):
    id: int

    class Config:
        orm_mode = True

class CarritoUpdate(CarritoBase):
    pass

class TarjetaBase(BaseModel):
    cliente_id: int
    numero: str

class TarjetaCreate(TarjetaBase):
    pass

class Tarjeta(TarjetaBase):
    id: int

    class Config:
        orm_mode = True
        
class TarjetaUpdate(TarjetaBase):
    pass