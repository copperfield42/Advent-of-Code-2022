#https://adventofcode.com/2022/day/21
from __future__ import annotations

from typing import Iterator, Iterable, NamedTuple, Callable
import itertools_recipes as ir
import operator
from fractions import Fraction

OPERATION = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": Fraction,
    "=": operator.eq
    }

test_input="""
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

class DelayedOP(NamedTuple):
    op:Callable[[int,int],int]
    x:str
    y:str


def process_data(data:str) -> Iterator[ tuple[str,int] | tuple[str,DelayedOP] ]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        name, calculo = line.split(":")
        calculo = calculo.strip()
        if calculo.isnumeric():
            yield name, int(calculo)
        else:
            x,op,y = calculo.split()
            yield name, DelayedOP(OPERATION[op],x,y)
        
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


