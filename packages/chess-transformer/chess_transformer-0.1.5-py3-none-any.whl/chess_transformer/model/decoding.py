from typing import Sequence
from jaxtyping import Float
import torch
import chess

def decode_file(file: int):
  return chr(file + ord('a'))

def decode_rank(rank: int):
  return str(rank + 1)

def decode_uci(from_file: int, from_rank: int, to_file: int, to_rank: int):
  return decode_file(from_file) + decode_rank(from_rank) + decode_file(to_file) + decode_rank(to_rank)

def decode_ucis(logits: Float[torch.Tensor, 'B L 37']) -> Sequence[Sequence[str]]:
  batch_size = logits.size(0)
  from_files = torch.argmax(logits[:, :, 0:8].reshape(batch_size, -1, 8), dim=-1)
  from_ranks = torch.argmax(logits[:, :, 8:16].reshape(batch_size, -1, 8), dim=-1)
  to_files = torch.argmax(logits[:, :, 16:24].reshape(batch_size, -1, 8), dim=-1)
  to_ranks = torch.argmax(logits[:, :, 24:32].reshape(batch_size, -1, 8), dim=-1)
  
  return [
    [
      decode_uci(*[int(i.item()) for i in idxs])
      for idxs in zip(from_files[b], from_ranks[b], to_files[b], to_ranks[b])
    ]
    for b in range(batch_size)
  ]

def ucis2pgn(ucis: Sequence[str]) -> Sequence[str]:
  """Parses UCIs into SAN. Stops whenever it finds an illegal move."""
  pgn = []
  board = chess.Board()
  try:
    for uci in ucis:
      move = chess.Move.from_uci(uci)
      pgn.append(board.san(move))
      board.push(move)
  finally:
    return pgn
  
def decode_pgns(logits: Float[torch.Tensor, 'B L 37']) -> Sequence[Sequence[str]]:
  return [ucis2pgn(ucis) for ucis in decode_ucis(logits)]