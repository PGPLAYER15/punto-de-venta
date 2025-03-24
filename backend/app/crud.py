from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas

### CRUD para Cliente ###

    # Crear un cliente

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(nombre=cliente.nombre, email=cliente.email)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

    # Obtener un cliente por id

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    # Obtener todos los clientes

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

### CRUD para Producto ###

    # Crear un producto    

def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(nombre=producto.nombre, precio=producto.precio, stock=producto.stock)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

    # Obtener un producto por id

def get_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

    # Obtener todos los productos

def get_productos(db: Session):
    return db.query(models.Producto).all()

### CRUD para  Carrito ###

    # Crear un carrito

def create_carrito(db: Session, carrito: schemas.CarritoCreate):
    db_carrito = models.Carrito(cliente_id=carrito.cliente_id, producto_id=carrito.producto_id, cantidad=carrito.cantidad)
    db.add(db_carrito)
    db.commit()
    db.refresh(db_carrito)
    return db_carrito

    # Obtener un carrito por id

def get_carrito(db: Session, carrito_id: int):
    return db.query(models.Carrito).filter(models.Carrito.id == carrito_id).first()

    # Obtener todos los carritos

### CRUD para Tarjeta ###

    # Crear una tarjeta

def create_tarjeta(db: Session, tarjeta: schemas.TarjetaCreate):
    db_tarjeta = models.Tarjeta(cliente_id=tarjeta.cliente_id, numero=tarjeta.numero)
    db.add(db_tarjeta)
    db.commit()
    db.refresh(db_tarjeta)
    return db_tarjeta

    # Obtener una tarjeta por id    

def get_tarjeta(db: Session, tarjeta_id: int):
    return db.query(models.Tarjeta).filter(models.Tarjeta.id == tarjeta_id).first()


# Similar para Tarjeta