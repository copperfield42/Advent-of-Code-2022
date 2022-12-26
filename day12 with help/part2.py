#https://adventofcode.com/2022/day/12
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import shortest_path_length_grid, vecinos2





def main(data:str) -> int:
    """part 2 of the puzzle """
    S,E,grid = process_data(data)
    a = grid[S]
    return shortest_path_length_grid(E, lambda p:grid[p]==a, grid, vecinos2)



def test() -> bool:
    return main(test_input) == 29



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













