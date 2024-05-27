from typing import NamedTuple, Sequence, Mapping, Callable
import random
import torch
from .dataset import FixedDataset, LazyDataset
from ..vocab import SpecialToken, MASK, PAD, Vocabulary

class MaskReturn(NamedTuple):
  masked_seq: Sequence[str | MASK]
  targets: Sequence[str | None]

def random_masking(
  seq: Sequence[str | PAD], *,
  mask_prob: float = 0.15
) -> MaskReturn:
  masked_seq = []
  targets = []
  for token in seq:
    if token != '[PAD]' and random.random() < mask_prob:
      masked_seq.append('[MASK]')
      targets.append(token)
    else:
      masked_seq.append(token)
      targets.append(None)

  return MaskReturn(masked_seq, targets)

class MaskedGame(NamedTuple):
  input_ids: torch.Tensor
  target_ids: torch.Tensor

def mask_game(
  seq: Sequence[str | PAD], vocab: Mapping[str | SpecialToken, int],
  *, mask_prob: float = 0.15
) -> MaskedGame:
  masked_seq, targets = random_masking(seq, mask_prob=mask_prob)
  input_ids = [vocab[move] for move in masked_seq]
  target_ids = [vocab[move] if move is not None else -100 for move in targets]

  return MaskedGame(torch.tensor(input_ids), torch.tensor(target_ids))

def fixed_masked_dataset(
  games: Sequence[Sequence[str]], vocab: Vocabulary,
  *, mask_prob: float = 0.15
) -> FixedDataset[MaskedGame]:
  
  max_len = max(len(game) for game in games)
  def sample(game: Sequence[str]) -> MaskedGame:
    padded_game = list(game) + ['[PAD]'] * (max_len - len(game))
    return mask_game(padded_game, vocab, mask_prob=mask_prob)

  return FixedDataset(games, sample)


def lazy_masked_dataset(
  game: Callable[[int], Sequence[str]], vocab: Vocabulary,
  *, num_games: int, mask_prob: float = 0.15, max_len: int
) -> LazyDataset[MaskedGame]:
  
  def sample(idx: int) -> MaskedGame:
    seq = game(idx)
    padded_game = list(seq) + ['[PAD]'] * (max_len - len(seq))
    return mask_game(padded_game, vocab, mask_prob=mask_prob)

  return LazyDataset(sample, num_games)