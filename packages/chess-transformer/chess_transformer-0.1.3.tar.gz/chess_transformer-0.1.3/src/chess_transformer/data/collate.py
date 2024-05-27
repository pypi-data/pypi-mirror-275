from typing import NamedTuple
from jaxtyping import Int
import torch

class PaddedBatch(NamedTuple):
  input_ids: Int[torch.Tensor, 'B L']
  target_ids: Int[torch.Tensor, 'B L']
  attention_mask: Int[torch.Tensor, 'B L']

def collate_fn(
  batch: list[tuple[torch.Tensor, torch.Tensor]], *,
  pad_token_id: int, ignore_idx: int = -100,
) -> PaddedBatch:
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
  
  return PaddedBatch(padded_input_ids, padded_target_ids, attention_mask)