from pydantic import BaseModel

class UserData(BaseModel):
    edad_cliente: int
    salario_cliente: float
    capital_prestado: float
    plazo_meses: int