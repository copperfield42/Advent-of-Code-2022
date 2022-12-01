#https://adventofcode.com/2022/day/1
#from __future__ import annotations


from typing import Iterator
import itertools_recipes as ir


test_input="""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def process_data(data:str) -> Iterator[int]:
    return (sum(map(int,x)) for x in ir.isplit(map(str.strip, data.splitlines()),""))

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def part1(data:str) -> int:
    """said how many calories carry the elves with the most calories"""
    return max(process_data(data))

def part2(data):
    """said how many calories carry the top 3 elves with the most calories"""
    data = sorted(process_data(data))
    return sum(data[-3:])



















