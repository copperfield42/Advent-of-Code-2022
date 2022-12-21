#https://adventofcode.com/2022/day/20
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import decrypt


def main(data:str) -> int:
    """part 1 of the puzzle """
    return decrypt(process_data(data))



def test() -> bool:
    return main(test_input) == 3



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1")
    data = get_raw_data()
    print("solution part1:", main(data)) #
    












