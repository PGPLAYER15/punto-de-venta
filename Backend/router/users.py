from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import hashlib

# Definimos el modelo para un usuario
class User(BaseModel):
    user_id: int
    phone_number: str
    email: str
    password: str  # La contraseña debe ser encriptada en producción

# Inicializamos el router para las rutas de usuarios
router = APIRouter()

# Lista de usuarios (deberías usar una base de datos real aquí)
users_db = []

# Registrar un nuevo usuario
@router.post("/users/", response_model=User)
async def register_user(user: User):
    # Aquí deberías encriptar la contraseña en producción
    user.password = hashlib.sha256(user.password.encode()).hexdigest()  # Simulando hash de la contraseña
    users_db.append(user)
    return user

# Obtener todos los usuarios
@router.get("/users/", response_model=List[User])
async def get_users():
    return users_db

# Obtener un usuario por ID
@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users_db:
        if user.user_id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Autenticación (solo un ejemplo básico, en un caso real debería ser más seguro)
@router.post("/login/")
async def login(user: User):
    for stored_user in users_db:
        if stored_user.email == user.email and stored_user.password == hashlib.sha256(user.password.encode()).hexdigest():
            return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
