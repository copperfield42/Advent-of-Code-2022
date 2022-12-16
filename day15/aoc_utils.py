#https://adventofcode.com/2022/day/15
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from functools import cached_property
import re
from dataclasses import dataclass
import numpy
import tqdm, sys
from scipy.signal import convolve2d
from multiprocessing import Pool
from functools import partial

progress_bar = tqdm.tqdm_gui if "idlelib" in sys.modules else tqdm.tqdm


test_input="""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""



def process_data(data:str) -> Iterator[Sensor]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        if hit := re.match("Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)",line):
            s1,s2, b1,b2 = map(int,hit.groups())
            yield Sensor( complex(s1,s2), complex(b1,b2) )


def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


def distance_t(point1:complex, point2:complex) -> float:
    new = point1 - point2
    return abs(new.real) + abs(new.imag)

@dataclass(eq=True, frozen=True)
class Sensor:
    position:complex
    beacon:complex

    @cached_property
    def min_distance(self) -> float:
        return distance_t(self.position,self.beacon)

    def __iter__(self):
        yield self.position
        yield self.beacon


def get_distances(sensors:Iterable[Sensor]) -> tuple[int,int,int,int,int]:
    min_x,max_x, min_y,max_y, max_d = float("inf"),-float("inf"),float("inf"),-float("inf"),0
    for s in sensors:
        max_d = max(max_d, s.min_distance)
        p = s.position  
        min_x = min(min_x,p.real)
        max_x = max(max_x,p.real)
        min_y = min(min_y,p.imag)
        max_y = max(max_y,p.imag)
    return tuple(map(int,(min_x,max_x, min_y,max_y, max_d)))


















