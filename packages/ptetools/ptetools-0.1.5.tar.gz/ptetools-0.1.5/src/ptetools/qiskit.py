from collections.abc import Sequence
from typing import overload

import numpy as np

from ptetools.tools import sorted_dictionary

CountsType = dict[str, int | float]


@overload
def counts2fractions(counts: Sequence[CountsType]) -> list[CountsType]:
    ...


@overload
def counts2fractions(counts: CountsType) -> CountsType:
    ...


def counts2fractions(counts: CountsType | Sequence[CountsType]) -> CountsType | list[CountsType]:
    if isinstance(counts, Sequence):
        return [counts2fractions(c) for c in counts]
    total = sum(counts.values())
    return sorted_dictionary({k: v / total for k, v in counts.items()})


def counts2dense(c: CountsType, number_of_bits: int) -> np.ndarray:
    """Convert dictionary with fractions or counts to a dense array"""
    d = np.zeros(2**number_of_bits, dtype=np.array(sum(c.values())).dtype)
    for k, v in c.items():
        idx = int(k.replace(" ", ""), base=2)
        d[idx] = v
    return d


if __name__ == "__main__":
    print(counts2dense({"1 0": 1.0}, 2))
    print(counts2fractions({"11": 20, "00": 30}))
    print(counts2fractions([{"11": 20, "00": 30}]))
