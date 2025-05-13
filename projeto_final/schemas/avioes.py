from pydantic import BaseModel
from datetime import datetime

class Aviao(BaseModel):
    modelo: str
    fabricante: str
    qtd_passageiros: int
    data_fabricacao: str
