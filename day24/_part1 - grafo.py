#https://adventofcode.com/2022/day/24
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Blizzards, Iterator, ir
from dataclasses import dataclass
import numpy
from aoc_recipes import Point, direcciones, progress_bar
import aoc_recipes
import networkx
from pprint import pprint


def vecinos(point:Point) -> Iterator[Point]:
    yield point
    yield from (p+point for p in direcciones.values())

def is_valid(point:Point|complex, shape:tuple[int,int]) -> bool:
    x,y = shape
    return 0<=point.real<x and 0<=point.imag<y

def make_vecinos(point, special, ronda, tablero) -> Iterator:
    if isinstance(point,str):
        point = special[point]
    for v in vecinos(point):
        if v in special:
            yield (ronda,special[v])
        elif is_valid(v,tablero.shape) and tablero[v]:
            yield (ronda,v)

def show_tablero(entrada, salida, blizzard, estado, nodes):
    X,Y = blizzard.shape
    bli = blizzard.ocupados_count()
    print( "".join(aoc_recipes.WHITE_char if entrada.y==i else "#" for i in range(-1,Y+1)))
    for x in range(X):
        print("#",end="")
        for y in range(Y):
            p = Point(x,y)
            if estado[p]:
                print(aoc_recipes.BLACK_char if p in nodes else aoc_recipes.WHITE_char, end="")
            else:
                if (b:=bli[p])>1:
                    print(b,end="")
                else:
                    print( next( c for c,v in blizzard.data.items() if v[p]), end="" )
        print("#")
    print( "".join(aoc_recipes.WHITE_char if salida.y==i else "#" for i in range(-1,Y+1)))
            

def main(data:str, show=False) -> int:
    """part 1 of the puzzle """
    entrada, salida, blizzard = process_data(data)
    print(entrada, salida, blizzard )
    G = networkx.DiGraph()
    campo = numpy.ones( blizzard.shape, dtype=bool )
    nodes = {(0,"E")}
    goal = {entrada:"E",
            salida:"S",
            "E":entrada,
            "S":salida}
    G.add_node( "E" )
    G.add_node( "S" )
    G.add_edge("E",(0,"E"))
    for ronda in progress_bar(ir.count(1)):
        next(blizzard)
        estado = campo ^ blizzard.ocupados()
        new_edges = {n:list(make_vecinos(n[-1],goal,ronda,estado)) for n in nodes}
        new_nodes = { n for lst in new_edges.values() for n in lst } #- nodes
        G.add_nodes_from(new_nodes)
        reach_exit = None
        if show:
            print("ronda",ronda)
            show_tablero(entrada, salida, blizzard, estado, {p for _,p in new_nodes})
            print("--------------------")       
        for n,veci in new_edges.items():
            for nn in veci:
                G.add_edge(n,nn)
                if "S" in nn or salida in nn:
                    reach_exit = nn
        if reach_exit:
            G.add_edge(reach_exit,"S")
            print("exit is reachable in round",ronda)
            break
        nodes = new_nodes
    return ronda,G


def test() -> bool:
    return main(test_input)[0] == 18



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)[0]) # 
    












