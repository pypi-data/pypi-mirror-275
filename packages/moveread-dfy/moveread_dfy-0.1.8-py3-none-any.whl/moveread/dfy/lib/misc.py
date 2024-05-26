import chess.pgn
import chess_pairings as cp

def update_pgns(games: cp.GamesMapping[chess.pgn.Game], tournId: str | None = None):
  ...