from jaxtyping import Int, Float
from torch import Tensor, nn

def loss(
  logits: Float[Tensor, 'batch seq_len 37'],
  labels: Int[Tensor, 'batch seq_len'], *,
  ce_loss: nn.CrossEntropyLoss = nn.CrossEntropyLoss()
) -> Float[Tensor, 'batch']:
  ...