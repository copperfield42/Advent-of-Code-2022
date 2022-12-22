#https://adventofcode.com/2022/day/22
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import simulate
                

def main(data:str, show=False) -> int:
    """part 1 of the puzzle """
    path, tablero = process_data(data)
    return simulate(path, tablero, lambda p,d,t: (p+d)%t.shape, show=show)



def test() -> bool:
    return main(test_input) == 6032



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1")
    data = get_raw_data()
    print("solution part1:", main(data)) # 122082
    












