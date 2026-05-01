from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.base import Base

class Heroi(Base):
    __tablename__ = "herois"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    classe = Column(String, nullable=False)
    nivel = Column(Integer, default=1)
    xp = Column(Integer, default=0)

    missoes = relationship('Missao', back_populates='herois')

    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.nivel = 1
        self.xp = 0

    def ganhar_experiencia(self, xp):
        self.xp += xp
        if self.xp >= 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.xp = 0

    def resumo(self):
        return f"[{self.id}] {self.nome} ({self.classe}) - Nivel {self.nivel} XP {self.xp}"
