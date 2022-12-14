#https://adventofcode.com/2022/day/14
#from __future__ import annotations

from typing import Iterator, NamedTuple
import itertools_recipes as ir
from functools import total_ordering, cached_property
from collections import UserList
import ast
from ast import literal_eval
import enum
from aoc_recipes import Point
from dataclasses import dataclass, field



test_input="""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

          


          
@dataclass(eq=True, frozen=True)
class Recta:
    ini:Point
    fin:Point

    def __iter__(self) -> Iterator[Point]:
        ini,fin = self.ini, self.fin
        diff = fin - ini
        assert diff.x == 0 or diff.y==0,"is not a vertical or horisontal recta"
        p = ini
        move = diff.normalize()
        while p != fin:
            yield p
            p = p + move
        yield p

    @cached_property
    def _members(self):
        return frozenset(self)

    def __contains__(self, other):
        if not isinstance(other, Point):
            return False
        return other in self._members

    def __len__(self):
        return len(self._members)

class Floor(Recta):

    def __init__(self, bottom:int):
        self.bottom = bottom
        super().__init__(Point(-float("inf"), bottom), Point(float("inf"), bottom))

    __iter__ = None
    __len__ = None

    def __contains__(self, other):
        if not isinstance(other, Point):
            return False
        _,y = other
        return y == self.bottom

    

direcciones_sand = [
    Point(0,1),
    Point(-1,1),
    Point(1,1),
    ]

@dataclass
class Cave:
    rocks:set[Point]
    sand_at_rest:set[Point] = field(init=False, default_factory=set)
    sand_origin:Point = Point(500,0)
    bottom:Floor = None
    _filled:bool = False


    @cached_property
    def abyss(self) -> int:
        return 3 + max( r.y for r in self.rocks )

    @property
    def is_filled(self):
        return self._filled

    @property
    def obstacles(self):
        if self.bottom is not None:
            return (self.sand_at_rest, self.rocks, self.bottom)
        return (self.sand_at_rest, self.rocks)

    def one_sand(self):
        if self.is_filled:
            return
        s = self.sand_origin
        while s.y <= self.abyss:
            move = False
            for d in direcciones_sand:
                new_s = s+d
                if any(new_s in r for r in self.obstacles):
                    continue
                s = new_s
                move = True
                break
            if not move:
                break
        if s.y < self.abyss:
            self.sand_at_rest.add(s)
        else:
            self._filled = True
        if s == self.sand_origin:
            self._filled = True




def make_cave(data:str, with_bottom:bool=False) -> Cave:
    rocks = set(ir.chain.from_iterable(process_data(data)))
    bottom = None
    if with_bottom:
        bottom = Floor(2 + max( r.y for r in rocks ) )
        
    return Cave( rocks, bottom = bottom)








def process_data(data:str) -> Iterator[Recta]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        yield from ( ir.starmap(Recta, ir.pairwise( Point(*literal_eval(x)) for x in line.split("->"))))
    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


def part1(data:str) -> int:
    """part 1 of the puzzle """
    cave = make_cave(data)
    while not cave.is_filled:
        cave.one_sand()
        
    return len(cave.sand_at_rest)
    


def part2(data:str) -> str:
    """part 2 of the puzzle """
    cave = make_cave(data,True)
    while not cave.is_filled:
        cave.one_sand()
    #print("sand:",len(cave.sand_at_rest))
    return len(cave.sand_at_rest)
     
    
 
    
   
def test1() -> bool:
    return part1(test_input) == 24

def test2() -> bool:
    return part2(test_input) == 93



data = get_raw_data()
assert test1(),"fail test 1"
print("pass test 1")
print("solution part1:", part1(data)) # 644
assert test2(),"fail test 2"
print("pass test 2")
print("solution part2:", part2(data)) # 27324














