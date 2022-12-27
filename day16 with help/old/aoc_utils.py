#https://adventofcode.com/2022/day/16
#from __future__ import annotations

from typing import Iterator, Iterable, Any
import itertools_recipes as ir
import re

from dataclasses import dataclass, field 
import itertools
from heapq import heappush, heappop


def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()





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











def process_data(data:str) -> Iterator[Valve]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        part1,part2 = line.split(";")
        name, flow_rate, connected = "","",[]
        if hit:=re.match("Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z\, ]+)",line):
            name, flow_rate, connected = hit.groups()
            yield Valve(name, int(flow_rate), tuple(connected.replace(",","").split()))


class PriorityQueue:

    def __init__(self):
        self._pq = []                         # list of entries arranged in a heap
        self._entry_finder = {}               # mapping of tasks to entries
        self._REMOVED = '<removed-task>'      # placeholder for a removed task
        self._counter = itertools.count()     # unique sequence count

    def __bool__(self):
        return bool(self._entry_finder)
        #return any(tk is not self._REMOVED for _,_,tk in self._pq)

    def __len__(self):
        return len(self._entry_finder)

    def add_task(self, task, priority:int=0):
        'Add a new task or update the priority of an existing task'
        if task in self._entry_finder:
            self.remove_task(task)
        count = next(self._counter)
        entry = [priority, count, task]
        self._entry_finder[task] = entry
        heappush(self._pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self._entry_finder.pop(task)
        entry[-1] = self._REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        pq = self._pq
        while pq:
            priority, count, task = heappop(pq)
            if task is not self._REMOVED:
                del self._entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')



@dataclass(order=True, eq=True, frozen=True)
class PrioritizedItem:
    priority: int
    item:Any = field(compare=False)







