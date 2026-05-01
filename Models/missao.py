from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.arquivoddados import Base, get_session

class Missao(Base):
    __tablename__ = "missoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    recompensa_xp = Column(Integer)
    status = Column(String, default="pendente")

    heroi_id = Column(Integer, ForeignKey("herois.id"))
    herois = relationship('Heroi', back_populates='missoes')

    def __init__(self, titulo, descricao, xp, heroi_id):
        self.titulo = titulo
        self.descricao = descricao
        self.recompensa_xp = xp
        self.heroi_id = heroi_id
        self.status = "pendente"

    def resumo(self):
     return f"[{self.id}] {self.titulo} - {self.status} (XP {self.recompensa_xp})"