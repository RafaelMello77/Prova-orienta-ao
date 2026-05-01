from Models.heroi import Heroi
from Models.missao import Missao
from Models.arquivoddados import get_session



def registrar_heroi(nome, classe):
    s = get_session()
    try:
        h = Heroi(nome, classe)
        s.add(h)
        s.commit()
        s.refresh(h)
        return h
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


def listar_herois():
    s = get_session()
    try:
        return s.query(Heroi).all()
    finally:
        s.close()


def buscar_heroi(id):
    s = get_session()
    try:
        return s.query(Heroi).filter_by(id=id).first()
    finally:
        s.close()


def remover_heroi(id):
    s = get_session()
    try:
        h = s.query(Heroi).filter_by(id=id).first()
        if h:
            s.query(Missao).filter_by(heroi_id=id).delete()
            s.delete(h)
            s.commit()
    finally:
        s.close()