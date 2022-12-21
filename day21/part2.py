#https://adventofcode.com/2022/day/21
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import DelayedOP, OPERATION
import operator
import poly # a library I make for simple polinomials calculations



def main(data:str, show=False) -> int:
    """part 2 of the puzzle """
    namespace = {}
    pendientes = {}
    OPERATION["/"] = operator.floordiv
    root = None
    for name, op in process_data(data):
        if name == "root":
            assert isinstance(op, DelayedOP)
            op = DelayedOP(OPERATION["="],op.x,op.y)
            root = op
            continue
        if name == "humn":
            assert isinstance(op, int)
            op = poly.x
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
    px = namespace[root.x] - namespace[root.y]
    if show:
        print("humn",namespace["humn"])
        print("root",root)
        print("x=",namespace[root.x])
        print("y=",namespace[root.y])
        print("equation to solve=",px)
    return int(poly.newton_root(px,0))


def test() -> bool:
    return main(test_input) == 301



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2")
    data = get_raw_data()
    print("solution part2:", main(data, show=True)) #
    













