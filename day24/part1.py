#https://adventofcode.com/2022/day/24
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import shortest_path_length




def main(data:str, show:bool=False):
    """part 1 of the puzzle """
    return shortest_path_length(*process_data(data), show=show)


def test() -> bool:
    return main(test_input) == 18


if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) #













