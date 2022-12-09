#https://adventofcode.com/2022/day/9
from __future__ import annotations

from typing import Iterator, NamedTuple
import itertools_recipes as ir
#import math
from math import copysign
#import collections

test_input="""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

test_input2 ="""
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, otro:Point):
        x,y = self
        if isinstance(otro,type(self)):
            ox, oy = otro
        elif isinstance(otro, (int,float)):
            ox, oy = otro,otro
        else:
            return NotImplemented
        return type(self)(x+ox, y+oy)

    def __radd__(self, otro:Point):
        return self + otro

    def __neg__(self):
        x,y = self
        return type(self)(-x, -y)

    def __sub__(self, otro:Point):
        return self + (-otro)

    def normalize(self):
        x,y = self
        return type(self)(x and int(copysign(1,x)),y and int(copysign(1,y)))

direcciones={
    "R":Point(1,0),
    "L":Point(-1,0),
    "U":Point(0,1),
    "D":Point(0,-1),
    }

touching = {*(map(sum,ir.combinations(direcciones.values(),2))),*direcciones.values()}

class State(NamedTuple):
    H: Point
    T: Point | list[Point]


class Tablero:

    def __init__(self):
        self.moves = [State(Point(0,0),Point(0,0))]

    def moveT(self, T:Point, H:Point) -> Point:
        if T==H:
            return T
        dis = H-T
        if dis in touching:
            return T
        return T + (dis).normalize()
        

    def play(self, moves:tuple[str,int]):
        move = direcciones[moves[0]]
        H,T = self.moves[-1]
        for _ in range(moves[1]):
            newH = H + move
            newT = self.moveT(T,newH)
            self.moves.append(State(newH,newT))
            H,T = newH, newT

    def show(self, max_x, max_y):
        for s in self.moves:
            if s is None:
                print("###############")
                continue
            H,T = s
            for y in range(max_y):
                for x in range(max_x):
                    P = Point(x,y)
                    c="."
                    if (H == P and T == H) or H==P:
                        c="H"
                    elif T == P:
                        c="T"
                    
                    print(c,end="")
                print()
            print("-----------------------")
            
class TableroN(Tablero):

    def __init__(self, size=10):
        self.moves = [State(Point(0,0),[Point(0,0) for _ in range(size-1)]) ]

    def play(self, moves:tuple[str,int]):
        move = direcciones[moves[0]]
        H,Tails = self.moves[-1] 
        for _ in range(moves[1]):
            newH = H + move
            newTails = []
            h = newH
            for T in Tails:
                newT = self.moveT(T,h)
                newTails.append(newT)
                h = newT
            self.moves.append(State(newH,newTails))
            H,Tails = newH, newTails
    show = None

    

def process_data(data:str) -> Iterator[tuple[str,int]]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data.splitlines()):
        d,n = line.split()
        yield d, int(n)
    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



def part1(data:str) -> int:
    """part 1 of the puzzle """
    board = Tablero()
    for play in process_data(data):
        board.play(play)
    return len( {s.T for s in board.moves })
    

def part2(data:str) -> int:
    """part 2 of the puzzle """
    board = TableroN()
    for play in process_data(data):
        board.play(play)
    return len( {s.T[-1] for s in board.moves })
     
    
 
    
   
def test1() -> bool:
    return 13 == part1(test_input)

def test2() -> bool:
    return 1 == part2(test_input) and 36 == part2(test_input2)


#test = part1(test_input)
#test.show(6,5)


data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 6271
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 2458














