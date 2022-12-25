#https://adventofcode.com/2022/day/25
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


SNAFU = {
    "2":2,
    "1":1,
    "0":0,
    "-":-1,
    "=":-2,
}
SNAFU.update({v:k for k,v in SNAFU.items()})

_CONVERSION = {k%5:k for k in (-2,-1,0,1,2)}

test_input="""
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
"""

def from_snafu(num:str) -> int:
    return sum( SNAFU[c]*(5**i) for i,c in enumerate(reversed(num)))  

def digits_snafu(num) -> Iterator[str]:
    if num<0:
        raise ValueError
    if num==0:
        yield SNAFU[0]
        return
    while num:
        num, d = divmod(num,5)
        d = _CONVERSION.get(d,d)
        if d<0:
            num += 1
        yield SNAFU[d]

def to_snafu(num:int) -> str:
    return "".join(reversed(list(digits_snafu(num))))
    


def process_data(data:str) -> Iterator[int]:
    """transform the raw data into a procesable form"""
    return map(from_snafu, ir.interesting_lines(data))
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


