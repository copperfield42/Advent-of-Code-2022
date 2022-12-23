#https://adventofcode.com/2022/day/23
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import numpy


DIRECTIONS = {
    "N" : 0-1j,
    "S" : 0+1j,
    "E" : 1+0j,
    "W" :-1+0j,
    "NE": 1-1j,
    "NW":-1-1j,
    "SE": 1+1j,
    "SW":-1+1j,
}


test_input="""
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

result_test_1="""
......#.....
..........#.
.#.#..#.....
.....#......
..#.....#..#
#......##...
....##......
.#........#.
...#.#..#...
............
...#..#..#..
"""

def process_data(data:str) -> Iterator[complex]:
    """transform the raw data into a procesable form"""
    for y,line in enumerate(ir.interesting_lines(data)):
        for x, char in enumerate(line):
            if char == "#":
                yield complex(x,y)
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


