#https://adventofcode.com/2022/day/2
#from __future__ import annotations


from typing import Iterator
#import itertools_recipes as ir
import functools

test_input="""A Y
B X
C Z
"""

@functools.total_ordering
class RPS:
    def __init__(self, pick:str):
        self.pick = {"A":"rock",
                     "X":"rock",
                     "C":"scissor",
                     "Z":"scissor",
                     "B":"paper",
                     "Y":"paper",
                     }[pick]
        
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.pick == other.pick

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        if self.pick == "rock" and other.pick == "scissor":
            return True
        if self.pick == "scissor" and other.pick == "paper":
            return True
        if self.pick == "paper" and other.pick == "rock":
            return True
        return False

    def __repr__(self):
        return f"<{self.pick}>"

    @property
    def shape(self) -> int :
        return 1 + ["rock","paper","scissor"].index(self.pick)

    def play(self,other) -> int:
        if not isinstance(other, type(self)):
            raise ValueError("not a RPS")
        if self == other:
            return 3
        if self > other:#you won
            return 6
        return 0#you lose

    def score(self,other) -> int:
        return self.play(other) + self.shape

    def reverse_pick(self):
        return {"rock":"X",
                "scissor":"Z",
                "paper":"Y",
                }[self.pick]

    def cmp(self,other) -> int:
        if self == other:
            return 0
        if self > other:
            return 1
        return -1

    def play_option(self):
        return sorted(list(map(RPS,"ABC")),key=lambda x: self.cmp(x))

    


def process_data(data:str) -> Iterator[tuple[RPS,RPS]]:
    for line in filter(None,map(str.strip, data.splitlines())):
        yield tuple(map(RPS,line.split()))

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def part1(data:str) -> int:
    """score if everything goes according to your strategy"""
    return sum( you.score(elve) for elve,you in process_data(data))

def part2(data):
    """ """
    resul=0
    for elve,you in process_data(data):
        y=elve.play_option()["ZYX".index(you.reverse_pick())]
        resul += y.score(elve)
    return resul



















