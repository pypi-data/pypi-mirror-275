from typing import Sequence, NamedTuple
from jaxtyping import Int
from torch import Tensor
import torch
from haskellian import iter as I
from .. import Vocabulary, vocab as default_vocab, parse_sample as _parse_sample

class Sample(NamedTuple):
  input_ids: Int[Tensor, 'seq_len']
  word_ends: Sequence[int]
  labs: Int[Tensor, 'seq_len 5']

class Batch(NamedTuple):
  input_ids: Int[Tensor, 'batch seq_len']
  word_ends: Sequence[Sequence[int]]
  labs: Int[Tensor, 'batch seq_len 5']

def parse_sample(line: str, vocab: Vocabulary = default_vocab) -> Sample:
  (tokens, ends), labs = _parse_sample(line)
  input_ids = [vocab[tok] for tok in tokens]
  return Sample(torch.tensor(input_ids), ends, torch.tensor(labs))

def collate_fn(batch: Sequence[Sample], *, max_len: int, pad_token_id: int, ignore_idx: int = -100) -> Batch:

  input_ids, ends, labs = I.unzip(batch)
  batch_size = len(input_ids)
  max_len = min(max(len(x) for x in input_ids), max_len)
  padded_input_ids = torch.full((batch_size, max_len), fill_value=pad_token_id)
  padded_labs = torch.full((batch_size, max_len, 5), fill_value=ignore_idx)

  for i in range(batch_size):
    padded_input_ids[i, :len(input_ids[i])] = input_ids[i][:max_len]
    padded_labs[i, :len(labs[i])] = labs[i][:max_len]

  return Batch(padded_input_ids, ends, padded_labs)