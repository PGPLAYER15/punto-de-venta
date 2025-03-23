from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Definimos el modelo para el pago
class Payment(BaseModel):
    order_id: int
    payment_method: str  # Ejemplo: "Tarjeta", "Efectivo"
    amount: float

# Inicializamos el router para las rutas de pago
router = APIRouter()

# Lista de pagos (deberías usar una base de datos real aquí)
payments_db = []

# Procesar el pago
@router.post("/payments/", response_model=Payment)
async def process_payment(payment: Payment):
    # Lógica para procesar el pago (simulada aquí)
    if payment.amount <= 0:
        raise HTTPException(status_code=400, detail="El monto debe ser mayor a 0.")
    payments_db.append(payment)
    return payment
