from typing import Literal, Sequence, NamedTuple, Iterable
import chess
from ..vocab import Vocabulary

promotion_ids = dict(n=1, b=2, r=3, q=4)
def parse_promotion(piece: Literal['n', 'b', 'r', 'q'] | None) -> int:
  return 0 if piece is None else promotion_ids[piece]

def parse_uci(e2e4q: str) -> tuple[int, int, int, int, int]:
  from_file = ord(e2e4q[0]) - ord('a')
  from_rank = int(e2e4q[1]) - 1
  to_file = ord(e2e4q[2]) - ord('a')
  to_rank = int(e2e4q[3]) - 1
  promotion = parse_promotion(e2e4q[4] if len(e2e4q) == 5 else None) # type: ignore
  return from_file, from_rank, to_file, to_rank, promotion

def sans2ucis(sans: Sequence[str]) -> Iterable[str]:
  board = chess.Board()
  for san in sans:
    move = board.parse_san(san)
    yield move.uci()
    board.push(move)

def uci_labels(sans: Sequence[str]) -> Sequence[tuple[int, int, int, int, int]]:
  return [parse_uci(uci) for uci in sans2ucis(sans)]

class Sample(NamedTuple):
  input_ids: Sequence[int]
  labs: Sequence[tuple[int, int, int, int, int]]

def sample(sans: Sequence[str], vocab: Vocabulary) -> Sample:
  labs = uci_labels(sans)
  input_ids = [vocab[san] for san in sans]
  return Sample(input_ids, labs)