from Models.missao import Missao
from Models.heroi import Heroi
from Models.arquivoddados import get_session


def criar_missao(titulo, descricao, xp, heroi_id):
    s = get_session()
    try:
        m = Missao(titulo, descricao, xp, heroi_id)
        s.add(m)
        s.commit()
        s.refresh(m)
        return m
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


def concluir_missao(missao_id):
    s = get_session()
    try:
        m = s.query(Missao).filter_by(id=missao_id).first()

        if m and m.status != "concluida":
            h = s.query(Heroi).filter_by(id=m.heroi_id).first()

            m.status = 'concluida'
            
            h.ganhar_experiencia(m.recompensa_xp)

            s.commit()
            return m
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()