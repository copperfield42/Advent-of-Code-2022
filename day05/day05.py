#https://adventofcode.com/2022/day/5
#from __future__ import annotations


from typing import Iterator
import itertools_recipes as ir
#import functools
import re
import csv
import collections
from pprint import pprint

test_input="""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

movimiento = collections.namedtuple("movimiento","move from_ to")


def process_data(data:str) -> tuple[dict[str,collections.deque[str]],list[movimiento]]:
    config, rawmoves = ir.isplit(data.splitlines(),"")
    *rawrows,fieldname = config
    cleanrow = tuple(x.replace("    "," ") for x in rawrows)
    crates = collections.defaultdict(collections.deque)
    for row in csv.DictReader(cleanrow[::-1],fieldnames=fieldname.strip().split(),delimiter=" "):
        for key,value in row.items():
            if value:
                crates[int(key)].append(value)
    moves = []                
    for m in rawmoves:
        if (play:=re.match("move ([0-9]+) from ([0-9]+) to ([0-9]+)",m)):
            moves.append(movimiento(*map(int,play.groups())))
    
    return crates, moves
    
def apply_moves(crates, moves):
    for m in moves:
        for _ in range(m.move):
            crates[m.to].append(crates[m.from_].pop())
    return crates

def apply_moves2(crates, moves):
    for m in moves:
        pile = [crates[m.from_].pop() for _ in range(m.move)]
        crates[m.to].extend(pile[::-1])
    return crates
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



def part1(data:str) -> int:
    """part 1 fo the puzzle """
    result = apply_moves(*process_data(data))
    return "".join(value[-1][1:-1] for key,value in sorted(result.items(),key=lambda x:x[0]))
    

def part2(data:str) -> int:
    """part 2 fo the puzzle """
    result = apply_moves2(*process_data(data))
    return "".join(value[-1][1:-1] for key,value in sorted(result.items(),key=lambda x:x[0]))
   

assert "CMZ" == part1(test_input)
assert "MCD" == part2(test_input)
data = get_raw_data()
print("solution part1", part1(data))
print("solution part2", part2(data))














