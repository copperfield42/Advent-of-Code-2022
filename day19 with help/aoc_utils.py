#https://adventofcode.com/2022/day/19
from __future__ import annotations

from typing import Iterator, Iterable, NamedTuple
import itertools_recipes as ir
import re
from dataclasses import dataclass, InitVar, field, astuple
from functools import total_ordering
from math import ceil



test_input="""
Blueprint 1:  Each ore robot costs 4 ore.  Each clay robot costs 2 ore.  Each obsidian robot costs 3 ore and 14 clay.  Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2:  Each ore robot costs 2 ore.  Each clay robot costs 3 ore.  Each obsidian robot costs 3 ore and 8 clay.  Each geode robot costs 3 ore and 12 obsidian.
"""

VALID_ROBOT_TYPE = {#robot type and their order
    'geode':0,
    'obsidian':1,
    'clay':2,
    'ore':3,
    }

@total_ordering
class Robot(NamedTuple):
    rtype:int
    #cost of robot
    obsidian:int = 0
    clay:int     = 0
    ore:int      = 0

    def ingredientes(self):
        for r in reversed(range(1,4)):
            if costo:=self[r]:
                yield r,costo

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        if self.rtype == other.rtype:
            return self[1:] < other[1:]
        return self.rtype < other.rtype
        #return VALID_ROBOT_TYPE[self.rtype] < VALID_ROBOT_TYPE[other.rtype]


@dataclass(eq=True)
class Blueprint:
    id:int
    plan:tuple[Robot]
    maxspend:tuple[int,int,int,int] = field(init=False)

    def __post_init__(self):
        spend=[0]
        for i in range(1,4):
            spend.append( max(r[i] for r in self.plan) )
        self.maxspend=tuple(spend)

    def __hash__(self):
        return hash(astuple(self))

    def quality_level(self, time:int) -> int:
        return 0


class Cantidad(NamedTuple):
    geode:int    = 0
    obsidian:int = 0
    clay:int     = 0
    ore:int      = 0


def dfs(blueprint:Blueprint, time:int, cantidad:Cantidad, bots:Cantidad, cache:dict=None, callback:Callable[[int,int,int],None]=None):
    #https://www.youtube.com/watch?v=H3PSODv4nf0
    if cache is None:
        cache = {}
    if time <= 0: 
        if callback:
            callback(time,cantidad.geode,len(cache)) 
        return cantidad.geode
    key = time, cantidad, bots
    if key in cache:
        if callback:
            callback(time,cache[key],len(cache)) 
        return cache[key]
    maxval = cantidad.geode + ( bots.geode * time )
    for bot in blueprint.plan:
        if bot.rtype != VALID_ROBOT_TYPE["geode"] and bots[bot.rtype] >= blueprint.maxspend[bot.rtype]:
            continue
        wait = 0
        for ingrediente,costo in bot.ingredientes():
            if not bots[ingrediente]:
                break
            wait = max(wait, ceil((costo - cantidad[ingrediente])/bots[ingrediente]))
        else:#no break
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            new_cantidad = [ x+y*(wait+1) for x,y in zip(cantidad,bots)]
            for ingrediente,costo in enumerate(bot[1:],1 ):
                new_cantidad[ingrediente] -= costo
            for ingrediente in range(1,4):
                new_cantidad[ingrediente] = min(new_cantidad[ingrediente], blueprint.maxspend[ingrediente]*remtime)
            new_bots = Cantidad(*( (x + (1 if i==bot.rtype else 0)) for i,x in enumerate(bots)))
            
            maxval = max(maxval, dfs(blueprint,remtime,Cantidad(*new_cantidad),new_bots,cache,callback))
    cache[key] = maxval
    if callback:
        callback(time,maxval,len(cache))     
    return maxval
                        
        


def process_data(data:str) -> Iterator[Blueprint]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        if bn:=re.match("Blueprint (?P<bn>\d+)\:",line ):
            bn = int(bn.group(1))
        else:
            continue
        robots = []
        for robot in re.findall("Each ([a-z]+) robot costs (\d+ [a-z]+(?: and \d+ [a-z]+)?)",line ):
            name, cost = robot
            cost = cost.split(" and ")
            dcost={}
            for part in cost:
                n,cname = part.split()
                dcost[cname]=int(n)
            robots.append( Robot(VALID_ROBOT_TYPE[name], **dcost) )
        yield Blueprint(bn, tuple(sorted(robots)))



def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



