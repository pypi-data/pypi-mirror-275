from typing import Mapping, Literal, TypeAlias
import string

SpecialToken: TypeAlias = Literal['[PAD]', '[SEP]']
Vocabulary: TypeAlias = Mapping[str | SpecialToken, int]

chars = string.ascii_letters + string.digits + '-'
vocab: Vocabulary = { char: i for i, char in enumerate(chars) } | {
  '[PAD]': len(chars),
  '[SEP]': len(chars) + 1
}