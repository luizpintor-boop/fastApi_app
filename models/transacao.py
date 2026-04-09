from sqlmodel import SQLModel, Field
from datetime import date

class Transacao(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    valor: float
    data: date