#https://adventofcode.com/2022/day/16
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import re
from dataclasses import dataclass
from pprint import pprint
from collections import deque
from functools import cache





test_input="""
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""



@dataclass(eq=True, frozen=True)
class Valve:
    name:str
    flow_rate:int
    connected:tuple[str]



def prepare_data(data:str, show=False) -> tuple[ dict[str,dict[str,int]], dict[str,int], dict[str,Valve] ]:
    #https://www.youtube.com/watch?v=bLMj50cpOug
    valves = {}
    indices_bit_mask = {}
    for valve in process_data(data):
        valves[valve.name] = valve
        if valve.flow_rate:
            indices_bit_mask[valve.name] = len(indices_bit_mask)
    if show:
        print("valves")
        pprint(valves)
        print("indices_bit_mask")
        pprint(indices_bit_mask)

    distancias = {}

    for name,valve in valves.items():
        if valve.flow_rate==0 and valve.name!="AA":
            continue
        distancias[name] = {name:0, "AA":0}
        visited = {name}
        queue = deque( [(0,name)] )
        while queue:
            dist, pos = queue.popleft()
            for neighbor in valves[pos].connected:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if valves[neighbor].flow_rate:
                    distancias[name][neighbor] = dist + 1
                queue.append( (dist+1, neighbor) )
        del distancias[name][name]
        if name != "AA":
            del distancias[name]["AA"]
    if show:
        print("distancias")
        pprint(distancias)
    return distancias, indices_bit_mask, valves

def prepare_dfs(distancias:dict[str,dict[str,int]], indices_bit_mask:dict[str,int], valves:dict[str,Valve]) -> Callable[[int,str,int]]:

    @cache
    def dfs(time:int, valve:str, bitmask:int=0) -> int:
        maxval = 0
        for neighbor in distancias[valve]:
            bit = 1 << indices_bit_mask[neighbor]
            if bitmask & bit:
                continue
            remtime = time - distancias[valve][neighbor] - 1
            if remtime <= 0:
                continue
            maxval = max(maxval, dfs(remtime, neighbor, bitmask|bit) + valves[neighbor].flow_rate*remtime)
        return maxval

    return dfs





def process_data(data:str) -> Iterator[Valve]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        part1,part2 = line.split(";")
        name, flow_rate, connected = "","",[]
        if hit:=re.match("Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z\, ]+)",line):
            name, flow_rate, connected = hit.groups()
            yield Valve(name, int(flow_rate), tuple(connected.replace(",","").split()))






def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



