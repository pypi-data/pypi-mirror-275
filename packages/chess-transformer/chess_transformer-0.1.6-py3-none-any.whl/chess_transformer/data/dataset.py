from typing import Sequence, Generic, TypeVar, Callable
from torch.utils.data import Dataset

T = TypeVar('T')

class FixedDataset(Dataset, Generic[T]):
  def __init__(
    self, games: Sequence[Sequence[str]], sample: Callable[[Sequence[str]], T]
  ):
    self.games = games
    self.sample = sample

  def __len__(self) -> int:
    return len(self.games)

  def __getitem__(self, idx: int) -> T:
    game = self.games[idx]
    return self.sample(game)

class LazyDataset(Dataset, Generic[T]):
  def __init__(
    self, sample: Callable[[int], T], num_samples: int
  ):
    self.samples: dict[int, T] = {}
    self.sample = sample
    self.num_samples = num_samples

  def __len__(self) -> int:
    return self.num_samples

  def __getitem__(self, idx: int) -> T:
    if idx in self.samples:
      return self.samples[idx]
    else:
      x = self.sample(idx)
      self.samples[idx] = x
      return x