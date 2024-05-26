from typing import Sequence
from sqlmodel import Session, select
from moveread.dfy.types import Token

def list(session: Session, tournId: str) -> Sequence[str]:
  return session.exec(select(Token.token).where(Token.tournId == tournId)).all()

def delete(session: Session, tournId: str, token: str):
  stmt = select(Token).where(Token.tournId == tournId, Token.token == token)
  obj = session.exec(stmt).first()
  if obj:
    session.delete(obj)
    session.commit()

def create(session: Session, tournId: str, token: str):
  obj = Token(tournId=tournId, token=token)
  session.add(obj)
  session.commit()
