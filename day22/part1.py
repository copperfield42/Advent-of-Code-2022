#https://adventofcode.com/2022/day/22
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import simulate, numpy, MPoint

def move_rule(point:MPoint, direction:MPoint, tablero:numpy.ndarray[int,int]) -> tuple[MPoint,MPoint]:
    """return a new point in the given direction, and the new direction that is facing"""
    pos = point
    while tablero[ (new:=(pos+direction)%tablero.shape) ]==0:
        pos = new
    return new, direction


def main(data:str, show=False) -> int:
    """part 1 of the puzzle """
    path, tablero = process_data(data)
    return simulate(path, tablero, move_rule, show=show)



def test() -> bool:
    return main(test_input) == 6032



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 122082
    












