#https://adventofcode.com/2022/day/17
from __future__ import annotations

from aoc_utils import test_input, get_raw_data
from aoc_utils import Rocas, Jets, VerticalChamber, VerticalChamberLite
import itertools as it
from aoc_recipes import progress_bar 
import numpy

def main(data:str, simulate:int=2022, play_field:VerticalChamber=VerticalChamberLite, progress_bar=progress_bar) -> int:
    """part 1 of the puzzle """
    jets = Jets(data)
    chamber = play_field()
    ijets = iter(jets)
    try:
        for i,r in zip(progress_bar(range(simulate)),it.cycle(Rocas)):
            chamber.one_rock(r,ijets)
    finally:
        print(chamber)
        print("master rocks:",len(chamber.master_rock))
        if isinstance(chamber, VerticalChamberLite):
            print("compacted:",chamber.compact_counter)
    return chamber.tope.imag


def test() -> bool:
    return main(test_input) == 3068


class Simulator:
    
    def __init__(self, data:str, show=True, chamber_class=VerticalChamber):
        self.chamber = chamber_class()
        self.jets = Jets(data)
        self.ijets = iter(self.jets)
        self.irocks = it.cycle(Rocas)
        self.chamber.pprint()
        self.show = show
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.chamber.one_rock(next(self.irocks),self.ijets,self.show)
        
    def __str__(self):
        self.chamber.pprint()
        return ""


def part1():
    assert test(),"fail test part 1"
    print("pass test part 1")
    data = get_raw_data()
    print("solution part1:", main(data)) # 3177
    

if __name__ == "__main__":
    pass
    part1()








