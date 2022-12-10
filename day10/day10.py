#https://adventofcode.com/2022/day/10
#from __future__ import annotations

from typing import Iterator, Iterable, TypeVar
import itertools_recipes as ir
#import math
#from math import copysign
#import collections
T = TypeVar("T")

test_input="""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


def process_data(data:str) -> Iterator[int|None]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data.splitlines()):
        if line == "noop":
            yield None
        else:"addx"
            _,n = line.split()
            yield int(n)
    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def cathode_ray_tube(instructions:Iterable[int|None]):
    addx = 1
    for ins in instructions:
        if ins is None:
            yield addx
        else:
            yield addx
            yield addx
            addx += ins
            

def sample_signal(iterable:Iterable[T], first:int, interval:int) -> Iterator[T]:
    data = iter(iterable)
    yield next( x for i,x in enumerate(data,1) if i==first )
    yield from ( x for i,x in enumerate(data,1) if i%interval==0)

def part1(data:str) -> int:
    """part 1 of the puzzle """
    crt = enumerate(cathode_ray_tube(process_data(data)),1)
    return sum(i*x for i,x in sample_signal(crt,20,40))

def make_line(data:Iterable[int]) -> str:  
    return "".join( "#" if x-1<=p<=x+1 else "." for p,x in enumerate(data) )

def part2(data:str) -> str:
    """part 2 of the puzzle """    
    return "\n".join(map(make_line,ir.chunked(cathode_ray_tube(process_data(data)),40)))
     
    
 
    
   
def test1() -> bool:
    return 13140 == part1(test_input)

def test2() -> bool:
    return part2(test_input) =="""##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1:", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2:", part2(data), sep="\n") # 














