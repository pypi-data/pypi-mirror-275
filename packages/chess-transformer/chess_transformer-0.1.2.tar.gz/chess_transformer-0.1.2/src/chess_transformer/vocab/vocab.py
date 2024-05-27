from typing import Literal, Mapping, TypeAlias
from .sans import legal_sans

SpecialToken: TypeAlias = Literal['[PAD]', '[CLS]', '[SEP]', '[MASK]']
PAD: TypeAlias = Literal['[PAD]']
MASK: TypeAlias = Literal['[MASK]']
Vocabulary: TypeAlias = Mapping[str | SpecialToken, int]

def remove_symbols(san: str) -> str:
  """Remove check and mate symbols from a SAN move"""
  return san.replace('+', '').replace('#', '')

def legal(with_symbols: bool = False) -> Vocabulary:
  """Vocabulary containing all legal SAN moves
  - `with_symbols`: whether to include `+` and `#` (triples the size of the vocabulary, though)
  """
  words = { san: i for i, san in enumerate(legal_sans(with_symbols)) }
  return words | {
    '[PAD]': len(words),
    '[CLS]': len(words) + 1,
    '[SEP]': len(words) + 2,
    '[MASK]': len(words) + 3
  }