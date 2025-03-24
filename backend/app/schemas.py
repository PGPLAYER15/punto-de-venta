from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    email: str

class ClienteCreate(ClienteBase):
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

class TarjetaBase(BaseModel):
    cliente_id: int
    numero: str

class TarjetaCreate(TarjetaBase):
    pass

class Tarjeta(TarjetaBase):
    id: int

    class Config:
        orm_mode = True