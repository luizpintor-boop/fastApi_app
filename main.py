from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, select

from models.transacao import Transacao
from core.database import engine, get_session
from schema.transacaoUpdate import TransacaoUpdate

app = FastAPI()

@app.get("/transacoes")
def listar(session: Session = Depends(get_session)):
    return session.exec(select(Transacao)).all()

@app.post("/transacoes")
def criar(transacao: Transacao, session: Session = Depends(get_session)):
    session.add(transacao)
    session.commit()
    session.refresh(transacao)
    return transacao


@app.delete("/transacoes/{id}")
def deletar(id: int, session: Session = Depends(get_session)):
    transacao = session.get(Transacao, id)

    if not transacao:
        return {"erro": "Transação não encontrada"}

    session.delete(transacao)
    session.commit()

    return {"mensagem": "Deletado com sucesso"}



@app.patch("/transacoes/{id}")
def atualizar_parcial(
    id: int,
    dados: TransacaoUpdate,
    session: Session = Depends(get_session)
):
    transacao = session.get(Transacao, id)

    if not transacao:
        return {"erro": "Transação não encontrada"}

    dados_dict = dados.dict(exclude_unset=True)

    for campo, valor in dados_dict.items():
        setattr(transacao, campo, valor)

    session.add(transacao)
    session.commit()
    session.refresh(transacao)

    return transacao