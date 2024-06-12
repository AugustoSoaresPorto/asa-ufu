from pydantic import BaseModel

class AlunosSchema(BaseModel):
    nome: str
    idade: int
    email: str
    curso: str
    periodo: int
    cidade: str
    estado: str
    pais: str
    endereco: str
