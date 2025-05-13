from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Avioes(Base):
    __tablename__ = 'avioes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String(45), nullable=False)
    fabricante = Column(String(45), nullable=False)
    qtd_passageiros = Column(Integer, nullable=False)
    data_fabricacao = Column(String(45), nullable=False)

    def __str__(self):
        return f"Modelo: {self.modelo}, Fabricante: {self.fabricante}, Quantidade de Passageiros: {self.qtd_passageiros}, Data de Fabricação: {self.data_fabricacao}"

    
