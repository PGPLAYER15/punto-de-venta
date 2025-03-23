from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Ejemplo: Tabla de Usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    carrito = relationship("Carrito", back_populates="usuario", uselist=False)

# Ejemplo: Tabla de Productos
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

# Ejemplo: Tabla de Pedidos
class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    total = Column(Float, nullable=False)

class Carrito(Base):
    __tablename__ = "carritos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))  # Relación 1 a 1 con usuario
    items = relationship("ItemCarrito", back_populates="carrito")  # Relación 1 a muchos con items

class ItemCarrito(Base):
    __tablename__ = "items_carrito"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer, default=1)
    producto_id = Column(Integer, ForeignKey("productos.id"))  # Relación con producto
    carrito_id = Column(Integer, ForeignKey("carritos.id"))     # Relación con carrito

    producto = relationship("Producto")  # Acceso directo al producto
    carrito = relationship("Carrito", back_populates="items")
