from pydantic import BaseModel

class CursosSchema(BaseModel):
    nome: str
    carga_horaria: int
    periodo: int
    descricao: str
