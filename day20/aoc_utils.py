#https://adventofcode.com/2022/day/20
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from collections import deque


test_input="""
1
2
-3
3
-2
0
4
"""



def delete_index(d:deque, index:int):
    d.rotate(-index)
    d.popleft()
    d.rotate(index)
    
def scramble(mask:Iterable[Any], data:deque[tuple[int,Any]]) -> deque[tuple[int,Any]]:
    """mix up the data deque according to the mask in-place
       the data must be a enumeration of the mask"""
    N = len(data)-1
    result = data
    for item in enumerate(mask):
        x = item[1]
        if not x:
            continue
        p = result.index( item )
        new = (p+x)%N
        delete_index(result,p)
        result.insert(new,item)
    return result        


def decrypt(data:Iterable[int], key:int=1, mix:int=1, check:Iterable[int]=(1000,2000,3000)) -> int:
    original = [key*n for n in data]
    result = deque(enumerate(original))
    for _ in range(mix):
        result = scramble(original,result)
    message = [x for i,x in result]
    offset = message.index(0)
    M = len(message)    
    return sum( message[(p+offset)%M] for p in check)


def process_data(data:str) -> Iterator[int]:
    """transform the raw data into a procesable form"""
    return map(int,ir.interesting_lines(data))
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------
