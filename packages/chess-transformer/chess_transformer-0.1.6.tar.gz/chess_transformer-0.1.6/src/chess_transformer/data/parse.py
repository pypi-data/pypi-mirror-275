from typing import Sequence

def parse_line(sans: str) -> Sequence[str]:
  return sans.strip('\n').split(' ')