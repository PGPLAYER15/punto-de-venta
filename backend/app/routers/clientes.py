from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from ..database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

### REGISTRO DE CLIENTES ###

@router.post("/clientes/create", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_cliente(db=db, cliente=cliente)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/clientes/", response_model=list[schemas.Cliente])
def read_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db)

@router.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

@router.get("/clientes/email/{email}", response_model=schemas.Cliente)
def get_cliente_by_email(email: str, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente_by_email(db, email=email)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

### LOGIN DE CLIENTES ###

@router.post("/login/", response_model=schemas.Cliente)
def login(email: str, password: str, db: Session = Depends(get_db)):
    cliente = crud.verificar_user(db, email, password)
    if not cliente:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"message": "Login exitoso", "cliente_id": cliente.id}
