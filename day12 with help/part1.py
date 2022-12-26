#https://adventofcode.com/2022/day/12
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import shortest_path_length_grid, vecinos




def main(data:str) -> int:
    """part 1 of the puzzle """
    #https://www.youtube.com/watch?v=sBe_7Mzb47Y
    return shortest_path_length_grid(*process_data(data), neighbors=vecinos)


def test() -> bool:
    return main(test_input) == 31



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












