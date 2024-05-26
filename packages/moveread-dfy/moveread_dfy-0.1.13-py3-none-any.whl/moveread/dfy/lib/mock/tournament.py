from datetime import date
from sqlmodel import Session
from chess_pairings import PairingsSource, ChessResultsPairings
from moveread.dfy.types import Tournament
from ..pairings import create_tournament

ST_MARTI = Tournament(
  tournId='stmarti', name='XVIII Open Sant Martí', site='Barcelona',
  start_date=date(2023, 1, 1), end_date=date(2023, 1, 9), groups=['a', 'b']
)

ST_MARTI_PAIRINGS = dict(
  a=PairingsSource(ChessResultsPairings(db_key=741703)),
  b=PairingsSource(ChessResultsPairings(db_key=741704)),
)

def create_mock(session: Session):
  create_tournament(session, ST_MARTI, group_pairings=ST_MARTI_PAIRINGS, model='llobregat23')