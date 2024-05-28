from typing import NamedTuple, Sequence
from haskellian import iter as I
from jaxtyping import Int
import torch
from ..vocab import Vocabulary
from .parse import parse_line
from .labs import sample

class TorchSample(NamedTuple):
  input_ids: Int[torch.Tensor, 'L']
  labels: Int[torch.Tensor, 'L 5']

class TorchBatch(NamedTuple):
  input_ids: Int[torch.Tensor, 'B L']
  labels: Int[torch.Tensor, 'B L 5']

def torch_sample(idx: int, *, lines: Sequence[str], vocab: Vocabulary) -> TorchSample:
  line = lines[idx]
  sans = parse_line(line)
  input_ids, labs = sample(sans, vocab)
  return TorchSample(torch.tensor(input_ids), torch.tensor(labs))

def collate_fn(batch: Sequence[TorchSample], pad_token_id: int, ignore_idx: int = -100) -> TorchBatch:

  input_ids, labs = I.unzip(batch)
  batch_size = len(input_ids)
  maxlen = max(len(x) for x in input_ids)
  padded_input_ids = torch.full((batch_size, maxlen), fill_value=pad_token_id)
  padded_labs = torch.full((batch_size, maxlen, 5), fill_value=ignore_idx)

  for i in range(batch_size):
    l = len(input_ids[i])
    padded_input_ids[i, :l] = input_ids[i]
    padded_labs[i, :l] = labs[i]

  return TorchBatch(padded_input_ids, padded_labs)
