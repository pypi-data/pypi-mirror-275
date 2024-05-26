from typing import Sequence, Mapping, Literal, Any
from haskellian import Either, Left, Right
from sqlmodel import Session, select
import chess_pairings as cp
from scoresheet_models import ModelID
from moveread.dfy.types import Tournament, Group, Pairings, SheetModel, Game, Pairing
from . import queries

def create_tournament(
  session: Session, tnmt: Tournament, *,
  group_pairings: Mapping[str, cp.PairingsSource] = {},
  model: ModelID | None = None,
):
  for name in tnmt.groups:
    group = Group(tournId=tnmt.tournId, name=name, rounds=[])
    session.add(group)

  for group, pairings in group_pairings.items():
    session.add(Pairings(tournId=tnmt.tournId, group=group, pairings=pairings))

  if model:
    session.add(SheetModel(tournId=tnmt.tournId, model=model))

  session.add(tnmt)
  session.commit()
  


def insert_pairings(session: Session, *, tournId: str, group: str, pairings: cp.GroupPairings) -> Sequence[cp.GameId]:
    """Inserts pairings to games that didn't already exist"""
    group_games = session.exec(queries.select_group_games(tournId, group)).all()
    games_idx = cp.GamesMapping.from_pairs([(g.gameId(), g) for g in group_games])
    added: list[cp.GameId] = []

    for round, rnd_pairings in pairings.items():
      for board, pair in rnd_pairings.items():
        gid = cp.gameId(tournId, group, round, board)
        if not gid in games_idx:
          game = Game(tournId=tournId, group=group, round=round, board=board, index=int(board)-1, pairing=Pairing(pair))
          session.add(game)
          added.append(gid)
    
    session.commit()
    return added



async def update_pairings(session: Session, tournId: str) -> Either[Literal['no-pairings'], Mapping[str, Either[Any, Sequence[cp.GameId]]]]:
  """Inserts pairings if inexistent. If successful, returns a sequence added games"""
  pairings = session.exec(select(Pairings).where(Pairings.tournId == tournId)).all()
  
  if pairings == []:
    return Left('no-pairings')
  
  results = {}
  for p in pairings:
    pairs = await cp.scrape_pairings(p.pairings)
    if pairs.tag == 'left':
      results[p.group] = pairs
    else:
      added = insert_pairings(session, tournId=tournId, group=p.group, pairings=pairs.value)
      results[p.group] = Right(added)
    
  return Right(results)
