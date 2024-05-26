from typing import Unpack
from sqlmodel import select
from chess_pairings import GameId, RoundId
from moveread.dfy.types import Game, Tournament, Round

def group_games(tournId: str, group: str):
  return Game.tournId == tournId, Game.group == group

def round_games(tournId: str, group: str, round: str):
  return Game.tournId == tournId, Game.group == group, Game.round == round

def exact_game(tournId: str, group: str, round: str, board: str):
  return Game.tournId == tournId, Game.group == group, Game.round == round, Game.board == board

def exact_round(tournId: str, group: str, round: str):
  return Round.tournId == tournId, Round.group == group, Round.name == round

def select_game(**gameId: Unpack[GameId]):
  return select(Game).where(*exact_game(**gameId))

def select_group_games(tournId: str, group: str):
  return select(Game).where(*group_games(tournId, group))

def select_tnmt(tournId: str):
  return select(Tournament).where(Tournament.tournId == tournId)

def select_round(**roundId: Unpack[RoundId]):
  return select(Round).where(*exact_round(**roundId))

def select_rounds(tournId: str, group: str):
  return select(Round).where(Round.tournId == tournId, Round.group == group)
