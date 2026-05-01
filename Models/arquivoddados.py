from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.base import Base

ENGINE = create_engine("sqlite:///tarefas.db", echo=False)

def criar_tabelas():
    Base.metadata.create_all(ENGINE)


def get_session():
    return sessionmaker(bind=ENGINE)()