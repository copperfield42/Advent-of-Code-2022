#https://adventofcode.com/2022/day/22
from __future__ import annotations

from typing import Iterable, Callable
import itertools_recipes as ir
from aoc_recipes import Point
import numpy
import re


class MPoint(Point):

    @property
    def row(self):
        return self.x
    @property
    def column(self):
        return self.y
    
    def __repr__(self):
        return f"{type(self).__name__}(row={self.x}, column={self.y})"

CHANGE_DIRECCION = {
    "R":-1j,
    "L":1j,
    }

DIRECCION = {#x=row y=column
    MPoint(0,1):">",
    MPoint(1,0):"v",
    MPoint(0,-1):"<",
    MPoint(-1,0):"^",
}
DIRECCION.update( [(v,k) for k,v in DIRECCION.items()] )


test_input="""
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""

def point_score(position:Point, direction:Point) -> int:
    return 1000*position.x + 4*position.y + ">v<^".index(DIRECCION[direction])


def simulate(path:Iterable[int|str], tablero:numpy.ndarray[int,int], move_rule:Callable[[Point,Point,numpy.ndarray[int,int]],tuple[Point,Point]], show=False) -> int:
    ini  = MPoint(1,numpy.where(tablero[1]==1)[0].min())
    move = DIRECCION[">"]
    pos  = ini
    print(f"inicial {pos=} {move=} {tablero.shape=}")
    for x in path:
        if show: print(x,DIRECCION[move],end=" ")
        if isinstance(x,int):
            if show: print(pos,end="->")
            for _ in range(x):
                new, new_move = move_rule(pos, move, tablero)
                match tablero[new]:
                    case 1:
                        pos, move = new, new_move
                    case -1:
                        break
                    case _:
                        raise RuntimeError("Unexpected value for tablero")
            if show: print(pos,end=" ")
        else:
            move = move*CHANGE_DIRECCION[x]
        if show: print(DIRECCION[move])
    print(f"final {pos=} {move=}")
    return point_score(pos, move)


def process_data(data:str) -> tuple[list[int|str], numpy.ndarray[int,int]]:
    """transform the raw data into a procesable form"""
    stablero, (path,) = ir.isplit(data.splitlines())
    path = [int(x) if x.isnumeric() else x for x in re.findall("(\d+|[RL])",path)]
    sizeX = max(map(len,stablero))+2
    tablero = numpy.zeros( (len(stablero)+2,sizeX), dtype=int)
    for x,row in enumerate(stablero,1):
        for y,tile in enumerate(row,1):
            match tile:
                case ".":
                    tablero[x,y]=1
                case "#":
                    tablero[x,y]=-1
    return path, tablero

    
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



