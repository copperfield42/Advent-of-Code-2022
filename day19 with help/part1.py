#https://adventofcode.com/2022/day/19
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Robot, Blueprint, Cantidad, dfs, Robot
from collections import defaultdict
from pprint import pprint
from aoc_recipes import progress_bar



def main(data:str) -> int:
    """part 1 of the puzzle """
    blueprints = {b.id:b for b in process_data(data)}
    pprint(blueprints)
    
    result = []
    for b in progress_bar(blueprints.values(), position=0):
        with progress_bar(position=1) as pbar:
            result.append( (b.id,dfs(b,24,Cantidad(),Cantidad(ore=1), callback=lambda t,m,c:pbar.set_postfix_str(f"{t=}, {m=}, {c=}",refresh=False) or pbar.update(1)  )) )
    pprint( result  )
    return sum( x*y for x,y in result )


def test() -> bool:
    return main(test_input) == 33



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1")
    data = get_raw_data()
    print("solution part1:", main(data)) # 1613
    












