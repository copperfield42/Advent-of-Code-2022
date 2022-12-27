#https://adventofcode.com/2022/day/16
from __future__ import annotations

#TODO look up the traveling salesman problem
#maybe use a priority queque

from typing import Iterable

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Valve, PriorityQueue, PrioritizedItem


import numpy
import networkx #https://networkx.org/
from networkx import shortest_path
import matplotlib.pyplot as plt
from pprint import pprint
from functools import partial


def make_grafo(valves:Iterable[Valve]|str):
    if isinstance(valves,str):
        valves = set(process_data(valves))
    grafo = networkx.DiGraph()
    for v in valves:
        grafo.add_node(v.name, flow=0)
        if v.flow_rate:
            grafo.add_node(v.name+"open", flow=v.flow_rate)
    for v in valves:
        grafo.add_edges_from( (v.name,x) for x in v.connected )
        if v.flow_rate:
            grafo.add_edges_from( (v.name+"open",x) for x in v.connected )
            grafo.add_edge(v.name, v.name+"open")
    return grafo


def show(G):
    #plt.subplot()
    #plt.axis("off")  #
    networkx.draw_kamada_kawai(G, with_labels=True, arrows=True)
    plt.show()

def preasure_release(path, valves, time=30):
    if time<=0:
        return 0
    preasure = 0
    for p in path:
        preasure += time * valves.get(p,0)
        time -= 1
        if not time:
            break
    #print("remaining time",time,"preasure release",preasure)
    return preasure

def all_paths(grafo, por_visitar:frozenset, path):
    if not por_visitar:
        yield path
    source = path[-1]
    if "open" in source:
        source = source[:2]
    for n in por_visitar:
        new = shortest_path(grafo,source,n)
        yield from all_paths(grafo, por_visitar.difference( (n,) ), path+new[1:])

def get_path(grafo, source="AA"):
    required = {n for n in grafo.nodes if "open" in n}
    flow = {n:grafo.nodes[n]["flow"] for n in required}
    priority = partial( preasure_release, valves=flow)
    path = (source,)
    task = PrioritizedItem( priority(path), [path, frozenset(required)])
    pqueue = PriorityQueue()
    pqueue.add_task( task )
    while pqueue:
        path,required = pqueue.pop_task().item
        if not required:
            yield priority(path),path
            continue
        for node in required:
            new_path = shortest_path(grafo, path[-1], node)
            new_path = path + tuple(new_path[1:])
            task = PrioritizedItem( priority(new_path), [new_path, required.difference((node,))])
            pqueue.add_task( task )
        
        
        
    
                        

def main(data:str) -> int:
    """part 1 of the puzzle """
    valves = {v.name:v for v in process_data(data)}
    grafo = make_grafo(valves.values())
    required = {n for n in grafo.nodes if "open" in n}
    flow = {n:valves[n[:2]].flow_rate for n in required}
    print(required)
    print(flow)
    source = "AA"
    mega_path = max(all_paths(grafo,frozenset(required),["AA"]), key=lambda x:preasure_release(x,flow))
    print("calculation ready")
    print(mega_path)
    return preasure_release(mega_path, flow)
    return grafo


def test() -> bool:
    return main(test_input) == 1651


def part1():
    assert test(),"fail test part 1"
    print("pass test part 1")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    
if __name__ == "__main__":
    #part1()
    pass



G = make_grafo(test_input)
#show(G)

pqueue = PriorityQueue()





