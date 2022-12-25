#https://adventofcode.com/2022/day/24
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import shortest_path_length as spl





def main(data:str) -> int:
    """part 2 of the puzzle """
    entrada, salida, blizzard = process_data(data)
    p1 = spl(entrada, salida, blizzard)
    p2 = spl(salida, entrada, blizzard, counter=p1)
    return spl(entrada, salida, blizzard, counter = p2)


def test() -> bool:
    return main(test_input) == 54



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #














