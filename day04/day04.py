#https://adventofcode.com/2022/day/4
#from __future__ import annotations


from typing import Iterator
import itertools_recipes as ir
#import functools

test_input="""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""




def process_data(data:str) -> Iterator[list[tuple[int,int]]]:
    for line in ir.interesting_lines(data.splitlines()):
        yield [tuple(map(int,p.split("-"))) for p in line.split(",")]

def is_contain(a:tuple[int,int], b:tuple[int,int]) -> bool:
    x1,y1 = a
    x2,y2 = b
    return (x1<=x2 and y2<=y1) or (x2<=x1 and y1<=y2)

def overlap(a:tuple[int,int], b:tuple[int,int]) -> bool:
    x1,y1 = a
    x2,y2 = b
    return ((x1<=x2<=y1) or (x1<=y2<=y1)) or \
           ((x2<=x1<=y2) or (x2<=y1<=y2))

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def part1(data:str) -> int:
    """said how many assigment pair does one fully contain the other """
    return sum( is_contain(*x) for x in process_data(data))


def part2(data:str) -> int:
    """ """
    return sum( overlap(*x) for x in process_data(data))



















