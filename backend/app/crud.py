from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from passlib.context import CryptContext
### CRUD para Cliente ###
    # Crear un cliente

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.email == cliente.email).first()
    if db_cliente:
        raise ValueError("El correo electrónico ya está registrado.")
    
    hashed_password = pwd_context.hash(cliente.password)
    db_cliente = models.Cliente(
        nombre=cliente.nombre,
        email=cliente.email,
        password=hashed_password 
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def verificar_user(db: Session, email: str, password: str):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.email == email).first()
    if not db_cliente:
        return None
        # Verificar la contraseña
    if not pwd_context.verify(password, db_cliente.password):
        return None
    return db_cliente

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    # Obtener un cliente por email

def get_cliente_by_email(db: Session, email: str):
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()

    # Obtener todos los clientes

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

    # Actualizar un cliente

def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteUpdate):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        raise ValueError("Cliente no encontrado.")

    db_cliente.nombre = cliente.nombre
    db_cliente.email = cliente.email
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

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

    # Actualizar un producto
    
def update_producto(db: Session, producto_id: int, producto: schemas.ProductoUpdate):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    db_producto.nombre = producto.nombre
    db_producto.precio = producto.precio
    db_producto.stock = producto.stock
    db.commit()
    db.refresh(db_producto)
    return db_producto

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

    # Update un carrito

def update_carrito(db: Session, carrito_id: int, carrito: schemas.CarritoUpdate):
    db_carrito = db.query(models.Carrito).filter(models.Carrito.id == carrito_id).first()
    db_carrito.cliente_id = carrito.cliente_id
    db_carrito.producto_id = carrito.producto_id
    db_carrito.cantidad = carrito.cantidad
    db.commit()
    db.refresh(db_carrito)
    return db_carrito

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