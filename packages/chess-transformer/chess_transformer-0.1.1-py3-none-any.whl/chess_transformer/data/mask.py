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
  *, mask_prob: float = 0.15, ignore_idx: int = -100
) -> MaskedGame:
  masked_seq, targets = random_masking(seq, mask_prob=mask_prob)
  input_ids = [vocab[move] for move in masked_seq]
  target_ids = [vocab[move] if move is not None else ignore_idx for move in targets]

  return MaskedGame(torch.tensor(input_ids), torch.tensor(target_ids))

def fixed_masked_dataset(
  games: Sequence[Sequence[str]], vocab: Vocabulary,
  *, mask_prob: float = 0.15
) -> FixedDataset[MaskedGame]:
  
  def sample(game: Sequence[str]) -> MaskedGame:
    return mask_game(game, vocab, mask_prob=mask_prob)

  return FixedDataset(games, sample)


def lazy_masked_dataset(
  game: Callable[[int], Sequence[str]], vocab: Vocabulary,
  *, num_games: int, mask_prob: float = 0.15
) -> LazyDataset[MaskedGame]:
  
  def sample(idx: int) -> MaskedGame:
    seq = game(idx)
    return mask_game(seq, vocab, mask_prob=mask_prob)

  return LazyDataset(sample, num_games)


def collate_fn(
  batch: list[tuple[torch.Tensor, torch.Tensor]], *,
  pad_token_id: int, ignore_idx: int = -100,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
  input_ids, target_ids = zip(*batch)
  
  max_length = max(len(ids) for ids in input_ids)
  
  padded_input_ids = torch.full((len(input_ids), max_length), fill_value=pad_token_id)
  padded_target_ids = torch.full((len(target_ids), max_length), fill_value=ignore_idx)
  attention_mask = torch.zeros((len(input_ids), max_length), dtype=torch.long)
  
  for i in range(len(input_ids)):
    length = len(input_ids[i])
    padded_input_ids[i, :length] = input_ids[i]
    padded_target_ids[i, :length] = target_ids[i]
    attention_mask[i, :length] = 1
  
  return padded_input_ids, padded_target_ids, attention_mask