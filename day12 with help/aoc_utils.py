#https://adventofcode.com/2022/day/12
from __future__ import annotations

from typing import Iterator
import string
import numpy
from aoc_recipes import Point,  make_vecinos, is_valid, shortest_path_length_grid, where, get_raw_data



alturas = {c:a for a,c in enumerate(string.ascii_lowercase,1)}
alturas["S"] = alturas["a"]-1
alturas["E"] = alturas["z"]+1



test_input="""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

def vecinos(point:Point, tablero:numpy.ndarray[int,int]) -> Iterator[Point]:
    return make_vecinos(point,lambda x:is_valid(x,tablero.shape) and tablero[x]<=tablero[point]+1)

def vecinos2(point:Point, tablero:numpy.ndarray[int,int]) -> Iterator[Point]:
    return make_vecinos(point,lambda x:is_valid(x,tablero.shape) and tablero[x]>=tablero[point]-1)


def process_data(data:str) -> tuple[Point,Point,numpy.ndarray[int,int]]:
    """transform the raw data into a procesable form"""
    points = [ list(map(alturas.get,line)) for line in data.split()]
    grid = numpy.array(points, dtype=int)
    S = Point(*next(where(grid == alturas["S"])))
    E = Point(*next(where(grid == alturas["E"])))
    grid[S] = alturas["a"]
    grid[E] = alturas["z"]
    return S,E,grid
    
    



