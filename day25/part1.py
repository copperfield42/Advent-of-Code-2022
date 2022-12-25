#https://adventofcode.com/2022/day/25
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import to_snafu, from_snafu





def main(data:str) -> str:
    """part 1 of the puzzle """
    return to_snafu(sum(process_data(data)))


def test() -> bool:
    return main(test_input) == "2=-1=0"



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












