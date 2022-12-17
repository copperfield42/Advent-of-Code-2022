#https://adventofcode.com/2022/day/17
#from __future__ import annotations

from typing import Iterator, Iterable, Literal
import itertools_recipes as ir
import numpy
from dataclasses import dataclass, field
from functools import partial




test_input="""
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""



def process_data(data:str) -> Iterator[tuple[Literal[-1,1],int]]:
    """transform the raw data into a procesable form"""
    for c,v in ir.groupby(data):
        n = ir.ilen(v)
        match c:
            case "<":
                yield (-1,n)
            case ">":
                yield (1,n)
                
        
    pass
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------
@dataclass
class Rock:
    points:numpy.ndarray[complex]

    def __str__(self):
        Xs = int(self.points.real.max()+1)
        Ys = int(self.points.imag.max()+1)
        return "\n".join( "".join("#" if complex(x,y) in self.points else " " for x in range(Xs))
                          for y in range(Ys)
                          )

def make_rock(data:list[str]) -> Rock:
    points = []
    for y,line in enumerate(ir.interesting_lines(reversed(data))):
        for x,c in enumerate(line):
            if c=="#":
                points.append(complex(x,y))
            elif c!=".":
                raise ValueError(f"unexpected character {c}")
    return Rock(numpy.array(points, dtype=complex))

rocks_models ="""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

    
Rocas = [make_rock(r) for r in ir.isplit(rocks_models.splitlines())]



class Jets:
    """
    jets of hot gas represented by an infinite sequences of 1 or -1
    in a ciclycal pattern according to its input

    "<" = -1
    ">" = 1

    """
    
    def __init__(self, patterns:str):
        """patterns is a string containing only "<" or ">" characters"""
        self.patron = tuple(process_data(patterns))

    def __iter__(self) -> Iterator[Literal[-1,1]]:
        return ir.chain.from_iterable( ir.repeat(v,n) for v,n in ir.cycle(self.patron))

    def __eq__(self, other) -> bool:
        if not isinstance(other,type(self)):
            return False
        return self.patron == otro.patron

    def __hash__(self):
        return hash(self.patron)

    def __getitem__(self, index) -> Literal[1,-1]:
        return ir.nth(self,index)


INITIAL_POSITION:complex = complex(2,4)

    

@dataclass
class VerticalChamber:
    wall_left:int = -1
    wall_right:int = 7
    tope:complex = 0j
    rocas:list[Rock] = field(default_factory = list, init=False, repr=False)
    falling_rock:numpy.ndarray[complex] = field(default_factory = partial(numpy.zeros,1,complex), init=False, repr=False)
    
    
    def one_rock(self, rock:Rock, jets:Iterator[Literal[1,-1]], show=False):
        rp = rock.points + ( self.tope + INITIAL_POSITION )
        move = ir.cycle( (True,False) )
        self.falling_rock = rp
        if show: print("new rock");self.pprint()
        for move in ir.cycle( (True,False) ):
            step = next(jets) if move else -1j
            new_rp = rp + step
            if self.colide(new_rp):
                if show: print("no move",f"jet of gas: {step}" if move else "fall");self.pprint()
                if not move:
                    break
                else:
                    continue 
            rp = new_rp
            self.falling_rock = rp
            if show: print(f"jet of gas: {step}" if move else "fall");self.pprint()
        self.add_rock( rp )
        if show: print("rock stops");self.pprint()
        
    def add_rock(self):
        self.rocas.append( Rock(rp) )
        self.tope = max(self.tope.imag, rp.imag.max())*1j
        self.falling_rock = numpy.zeros(1,complex)
        
    def colide(self, points:numpy.ndarray[complex]) -> bool:
        if (points.real==self.wall_left).any() or (points.real==self.wall_right).any() or (points.imag==0).any():
            return True #colide with a wall or reacheds the floor
        return any( len(numpy.intersect1d(points, r.points)) for r in reversed(self.rocas))

    def pprint(self):
        tope = int(self.tope.imag + (min(5,self.falling_rock.imag.max()) or 5))
        for y in reversed(range(1,tope)):
            print("|",end="")
            for x in range(self.wall_right):
                p = complex(x,y)
                c = '░'
                if p in self.falling_rock:
                    c = "@"
                elif any( p in r.points for r in self.rocas):
                    c = "#"  
                print(c,end="")
            print("|")
        print("+","-"*(self.wall_right),"+",sep="")
                    





























