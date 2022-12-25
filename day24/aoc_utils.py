#https://adventofcode.com/2022/day/24
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from dataclasses import dataclass
import numpy
from aoc_recipes import Point, direcciones, progress_bar, BLACK_char, WHITE_char
from pprint import pprint






@dataclass
class Blizzards:
    data:dict[str,numpy.ndarray[bool,bool]]
    #cycle:Point = None
    shape:tuple[int,int] = None

    def __post_init__(self):
        self.roll_karg = {
            "<":{"shift":-1, "axis":1},
            ">":{"shift":1, "axis":1},
            "^":{"shift":-1, "axis":0},
            "v":{"shift":1, "axis":0},
        }
        #self.cycle = Point(0,0)
        self.shape = self.data["<"].shape
        assert self.data.keys() == self.roll_karg.keys()

    def __iter__(self):
        return self

    def __getitem__(self, key:str) -> numpy.ndarray[bool,bool]:
        return self.data[key]

    def __next__(self):
        self.data = { k:numpy.roll(self.data[k],**karg) for k,karg in self.roll_karg.items() }
        #self.cycle = ( self.cycle + Point(1,1) ) % self.shape


    def __repr__(self):
        return f"<{type(self).__name__}({ dict( (k,v.sum()) for k,v in self.data.items())}, shape={self.shape})>"

    def ocupados(self) -> numpy.ndarray[bool, bool]:
        a,b,c,d = self.data.values()
        return a|b|c|d

    def ocupados_count(self) -> numpy.ndarray[int, int]:
        a,b,c,d = self.data.values()
        return (a*1)+b+c+d


test_input_1="""
#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#
"""
test_input="""
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""


def vecinos(point:Point) -> Iterator[Point]:
    yield point
    yield from (p+point for p in direcciones.values())

def is_valid(point:Point|complex, shape:tuple[int,int]) -> bool:
    x,y = shape
    return 0<=point.real<x and 0<=point.imag<y

def make_vecinos(point:Point, special:dict[str|Point,Point|str], tablero:numpy.ndarray[bool,bool]) -> Iterator[Point]:
    if isinstance(point,str):
        point = special[point]
    for v in vecinos(point):
        if v in special:
            yield special[v]
        elif is_valid(v,tablero.shape) and tablero[v]:
            yield v

def show_tablero(entrada:Point, salida:Point, blizzard:Blizzards, estado:numpy.ndarray[bool,bool], nodes:set[Point]):
    X,Y = blizzard.shape
    bli = blizzard.ocupados_count()
    print( "".join(WHITE_char if entrada.y==i else "#" for i in range(-1,Y+1)))
    for x in range(X):
        print("#",end="")
        for y in range(Y):
            p = Point(x,y)
            if estado[p]:
                print(BLACK_char if p in nodes else WHITE_char, end="")
            else:
                if (b:=bli[p])>1:
                    print(b,end="")
                else:
                    print( next( c for c,v in blizzard.data.items() if v[p]), end="" )
        print("#")
    print( "".join(WHITE_char if salida.y==i else "#" for i in range(-1,Y+1)))


def shortest_path_length(entrada:Point, salida:Point, blizzard:Blizzards, counter:int=0, show:bool=False,) -> int:
    print(entrada, salida, blizzard )
    campo = numpy.ones( blizzard.shape, dtype=bool )
    nodes = {"E"}
    goal = {entrada:"E",
            salida:"S",
            "E":entrada,
            "S":salida}
    ronda = counter
    counter += 1
    for ronda in progress_bar( ir.count(counter), initial=counter ):
        next(blizzard)
        estado = campo ^ blizzard.ocupados()
        new_nodes = set()
        for n in nodes:
            for nn in make_vecinos(n,goal,estado):
                if nn == "S":
                    return ronda
                new_nodes.add(nn)
        nodes = new_nodes
        if show:
            print("ronda",ronda)
            show_tablero(entrada, salida, blizzard, estado, nodes)
            print("--------------------")


def process_data(data:str) -> tuple[ Point, Point, Blizzards ]:
    """transform the raw data into a procesable form"""
    lines = data.strip().splitlines()
    X = len(lines[0])-2
    Y = len(lines)-2
    blizzard = {b:numpy.zeros( (Y,X), dtype=bool) for b in "<>^v" }
    for x,row in enumerate(lines,-1):
        for y,char in enumerate(row,-1):
            if char not in blizzard:
                continue
            blizzard[char][x,y] = True
    entrada = Point(-1,lines[0].index(".")-1)
    salida  = Point(len(lines)-2,lines[-1].index(".")-1)
    return entrada, salida, Blizzards(blizzard)



def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


