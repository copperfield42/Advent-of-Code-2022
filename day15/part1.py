#https://adventofcode.com/2022/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import distance_t, Sensor, get_distances

import numpy


def main(data:str, y_value:int) -> int:
    """part 1 of the puzzle """
    sensores = set(process_data(data))
    min_x,max_x, min_y,max_y, max_d = get_distances(sensores)
    M = numpy.arange(min_x - max_d, max_x+max_d) + complex(0,y_value)
    R = M==None
    for s in sensores:
        N = M - s.position
        N = abs(N.real) + abs(N.imag)
        R |=  (N<=s.min_distance)&(M!=s.beacon)
    return R.sum()


def test() -> bool:
    return main(test_input, y_value=10) == 26



data = get_raw_data()
assert test(),"fail test 1"
print("pass test 1")
print("solution part1:", main(data, y_value=2000000)) # 5809294
    












