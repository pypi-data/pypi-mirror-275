from typing import Iterable
import random
import chess

def random_move(board: chess.Board, rng = random.Random()) -> chess.Move | None:
  """A random legal move on the given position (if any)"""
  moves = list(board.legal_moves)
  if len(moves) == 0:
    return None
  idx = rng.randint(0, len(moves)-1)
  return moves[idx]

def random_sans(max_depth: int | None = None, rng = random.Random()) -> Iterable[str]:
  """A possibly-infinite line of legal moves, starting at `fen`"""
  board = chess.Board()
  mv = random_move(board)
  while mv is not None and (max_depth is None or board.ply() < max_depth):
    yield board.san(mv)
    board.push(mv)
    mv = random_move(board, rng)
  return board
