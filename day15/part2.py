#https://adventofcode.com/2022/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import distance_t, Sensor
from aoc_recipes import normalize

from typing import Iterable
import itertools_recipes as ir
from dataclasses import dataclass
import numpy




def tuning_frequency(beacon:complex|tuple[int,int]) -> int:
    if isinstance(beacon, (complex,float,int)):
        x,y = map(int,(beacon.real, beacon.imag))
    else:
        x,y = beacon
    return x*4000000 + y


@dataclass(eq=True, frozen=True)
class CircunferenceT:
    """2d discrete circunference in taxicab geometry or a Manhattan geometry"""
    center: complex
    radious: int
    
    def __len__(self):
        return int(4*self.radious)

    def __iter__(self) -> complex:
        c = self.center
        r = self.radious
        corners = [ c + r*d for d in (1,1j,-1,-1j)]
        corners.append(corners[0])
        for ini,fin in ir.pairwise(corners):
            yield ini
            path = normalize(fin-ini)
            p = ini+path            
            while p!=fin:
                yield p
                p = p+path
        

@numpy.vectorize
def is_detectable(point:complex, sensores:Iterable[Sensor]) -> bool:
    for s in sensores:
        if point in s:
            continue
        if distance_t(point, s.position) <= s.min_distance:
            return True
    return False

DIRECCIONES = numpy.array([complex(x,y) for x,y in ir.product([0,1,-1],repeat=2) if x or y])

@numpy.vectorize
def is_candidate(point:complex, sensores:Iterable[Sensor], to_ignore:set[complex], max_x:int, max_y:int) -> bool:
    if not ( 0 <= point.real <= max_x and 0 <= point.imag <= max_y):
        return False
    if point in to_ignore:
        return False
    test = is_detectable(DIRECCIONES + point, sensores)
    return test.all()
    

def main(data:str, show=False) -> int:
    """part 2 of the puzzle """
    sensores = set(process_data(data))
    circles ={CircunferenceT(s.position, s.min_distance+1) for s in sensores}
    know = {p for s in sensores for p in s}
    for i,c in enumerate(sorted(circles,key=len),1):
        if show: print(f"{i}/{len(circles)}",c,f"points = {len(c):_}",sep="\n")
        test = numpy.fromiter(c,dtype=complex)
        MD = is_detectable(test,sensores)
        MC = test[MD==False]
        if not len(MC):
            continue
        cand = is_candidate(MC, sensores, know, 4000000, 4000000)
        if cand.any():
            p = MC[cand][0]
            break
    if show: print(p)
    return tuning_frequency(p)


def test() -> bool:
    return main(test_input) == 56000011

if __name__=="__main__":
    assert test(),"fail test 2"
    print("pass test 2")
    data = get_raw_data()
    print("solution part2:", main(data, True)) # 10693731308112
    













