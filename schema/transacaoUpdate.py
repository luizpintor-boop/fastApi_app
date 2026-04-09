from sqlmodel import SQLModel
from typing import Optional
from datetime import date

class TransacaoUpdate(SQLModel):
    titulo: Optional[str] = None
    valor: Optional[float] = None
    data: Optional[date] = None