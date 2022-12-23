#https://adventofcode.com/2022/day/23
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from part1 import ElvesGrove
from itertools import count
from aoc_recipes import progress_bar




def main(data:str) -> int:
    """part 2 of the puzzle """
    play = ElvesGrove(process_data(data))
    for r in progress_bar(count(1)):
        if not play.round():
            break
    return r


def test() -> bool:
    return main(test_input) == 20



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













