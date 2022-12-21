#https://adventofcode.com/2022/day/21
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import DelayedOP




def main(data:str) -> int:
    """part 1 of the puzzle """
    namespace = {}
    pendientes = {}
    for name, op in process_data(data):
        if isinstance(op, DelayedOP):
            pendientes[name] = op
        else:
            namespace[name] = op
    while pendientes:
        for name, op in list(pendientes.items()):
            try:
                namespace[name] = op.op(namespace[op.x], namespace[op.y])
                del pendientes[name]
            except KeyError:
                pass
    return namespace["root"]
                
    


def test() -> bool:
    return main(test_input) == 152



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












