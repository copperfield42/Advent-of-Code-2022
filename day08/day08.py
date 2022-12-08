#https://adventofcode.com/2022/day/8
#from __future__ import annotations

from typing import Iterator
import numpy
import itertools_recipes as ir
from functools import partial
from math import prod

test_input="""
30373
25512
65332
33549
35390
"""





def process_data(data:str) -> "numpy.array[int]":
    """transform the raw data into a procesable form"""
    return numpy.array([list(map(int,row)) for row in ir.interesting_lines(data.splitlines())], dtype=int)
    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


def is_visible(data:numpy.array, x:int, y:int) -> bool:
    dx,dy = data.shape
    if (x==0 or x==dx-1) or (y==0 or y==dy-1):
        return True
    tree = data[x,y]
    return (data[x,y+1:] < tree).all() or \
           (data[x,:y] < tree).all()   or \
           (data[x+1:,y] < tree).all() or \
           (data[:x,y] < tree).all()

def view_count(tree:int, data:list[int]) -> int:
    view = 0
    for x in data:
        view += 1
        if x>=tree:
            break
    return view
    
def scenic_score(data:numpy.array, x:int, y:int) -> int:
    dx,dy = data.shape
    if (x==0 or x==dx-1) or (y==0 or y==dy-1):
        return 0
    tree = data[x,y]
    directions = data[x,:y][::-1], data[x,y+1:], data[x+1:,y], data[:x,y][::-1]
    return prod(map(partial(view_count,tree), directions))

def part1(data:str) -> int:
    """part 1 of the puzzle """
    grid = process_data(data)
    dx,dy = grid.shape
    return sum( is_visible(grid,x,y) for x in range(dx) for y in range(dy))
    
    

def part2(data:str) -> int:
    """part 2 of the puzzle """
    grid = process_data(data)
    dx,dy = grid.shape
    return max( scenic_score(grid,x,y) for x in range(dx) for y in range(dy))
    
 
    
   
def test1() -> bool:
    return 21 == part1(test_input)

def test2() -> bool:
    return 8 == part2(test_input)


#test = process_data(test_input)

data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 1854
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 527340














