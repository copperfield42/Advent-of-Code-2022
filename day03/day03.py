#https://adventofcode.com/2022/day/3
#from __future__ import annotations


from typing import Iterator
import itertools_recipes as ir
#import functools
import string
priority = " " + string.ascii_letters

test_input="""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""




def process_data(data:str) -> Iterator[tuple[str,str]]:
    for line in ir.interesting_lines(data.splitlines()):
        n = len(line)//2
        yield line[:n],line[n:]

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def part1(data:str) -> int:
    """sum of the priorities of the repeated item"""
    return sum( priority.index(set(c1).intersection(c2).pop())
                for c1,c2 in process_data(data)
                )


def part2(data:str) -> int:
    """sum of the priorities of the repeated item between elves team """
    return sum( priority.index( set(x[0]).intersection(*x[1:]).pop())
                for x in ir.chunked(ir.interesting_lines(data.splitlines()),3)
                )



















