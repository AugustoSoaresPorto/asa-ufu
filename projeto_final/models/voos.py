from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey, Float
from .database import Base

class Voos(Base):
    __tablename__ = 'voos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aeroporto_origem = Column(Integer, ForeignKey('aeroportos.id'), nullable=False)
    aeroporto_destino = Column(Integer, ForeignKey('aeroportos.id'), nullable=False)
    assentos_disponiveis = Column(Integer) 
    data = Column(String(45), nullable=False)
    preco = Column(Float)
    id_aviao = Column(Integer, ForeignKey('avioes.id'), nullable=False)
    
    def __str__(self): 
        return f"Aeroporto de Origem: {self.aeroporto_origem}, Aeroporto de Destino: {self.aeroporto_destino}, Assentos Disponíveis: {self.assentos_disponiveis}, Data: {self.data}, Preço: {self.preco:.2f}, ID do Avião: {self.id_aviao}"