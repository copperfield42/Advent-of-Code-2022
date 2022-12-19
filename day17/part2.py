#https://adventofcode.com/2022/day/17
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import VerticalChamberLite, Jets, Rocas
#from part1 import main 

from typing import Iterable, Any, Iterator, NamedTuple
from dataclasses import dataclass, field, InitVar
import itertools_recipes as ir


NUM_SIMUTATE = 1000000000000



@dataclass
class Cycler(Iterator):
    patron:InitVar[Iterable[Any]] = None
    ciclo:Iterator[tuple[int,Any]] = field(init=False, repr=False)
    estado:tuple[int,Any] =  field(init=False)

    def __post_init__(self, patron:Iterable[Any]):
        self.patron = patron = tuple(enumerate(patron))
        self.ciclo = ciclo = ir.cycle(patron)
        self.estado = next(ciclo)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.estado
        self.estado = next(self.ciclo)
        return value[-1]
    
    def __len__(self):
        return len(self.patron)
    
    @property
    def position(self):
        return self.estado[0]

    @property
    def value(self):
        return self.estado[1]



class Estado(NamedTuple):
    roca:int
    jet:int
    altura:int
    chamber:int
    pass


def find_cicle(data:str, simulate:int) -> tuple[list[Estado],list[Estado]]:
    jets = Cycler(process_data(data))
    rocas = Cycler(Rocas)
    chamber = VerticalChamberLite()
    history:dict[Estado,int] = {}
    tope = 0
    estados = []
    periodo = []
    for i in range(simulate):
        chamber.one_rock(next(rocas), jets)
        estado = Estado(rocas.position, jets.position, chamber.tope.imag-tope, chamber.estate())
        tope = chamber.tope.imag
        if estado in history:
            p = history[estado]
            periodo = estados[p:]
            estados = estados[:p]
            print("patron encontrado de len",len(periodo))
            break
        else:
            history[estado] = i
            estados.append( estado )
    return estados, periodo
        


def main(data:str, simulate:int) -> int:
    """part 2 of the puzzle """
    no_patron, patron = find_cicle(data, simulate)
    restantes = simulate - len(no_patron)
    mul,extra = divmod(restantes, len(patron))
    return sum(e.altura for e in no_patron) + mul*sum(e.altura for e in patron) + sum(e.altura for e in ir.islice(patron,extra))


def test() -> bool:
    return main(test_input, NUM_SIMUTATE) == 1514285714288


def part2():
    assert test(),"fail test part 2"
    print("pass test part 2")
    data = get_raw_data()
    print("solution part2:", main(data, NUM_SIMUTATE)) #
    
if __name__ == "__main__":
    part2()
    pass












