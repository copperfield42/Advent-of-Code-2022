#https://adventofcode.com/2022/day/18
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from ast import literal_eval
import numpy



test_input="""
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""



def process_data(data:str) -> Iterator[tuple[int,int,int]]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        yield literal_eval(line)
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------

def make_matrix(data:str) -> numpy.ndarray[bool,bool,bool]:
    points = list(process_data(data))
    size = max(map(max,points))+1
    matrix = numpy.zeros( (size,size,size), dtype=bool)
    for p in points:
        matrix[p]=True
    return matrix

