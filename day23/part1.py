#https://adventofcode.com/2022/day/23
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import DIRECTIONS, result_test_1
import aoc_recipes
import numpy
from dataclasses import dataclass
from functools import cache


nDIRECTIONS = numpy.fromiter(DIRECTIONS.values(), dtype=complex)

CHECK={
    "N":numpy.array([DIRECTIONS["N"],DIRECTIONS["NE"],DIRECTIONS["NW"]], dtype=complex),
    "S":numpy.array([DIRECTIONS["S"],DIRECTIONS["SE"],DIRECTIONS["SW"]], dtype=complex),
    "W":numpy.array([DIRECTIONS["W"],DIRECTIONS["NW"],DIRECTIONS["SW"]], dtype=complex),
    "E":numpy.array([DIRECTIONS["E"],DIRECTIONS["NE"],DIRECTIONS["SE"]], dtype=complex),
    }
CYCLE = "NSWE"
CARDINAL = {DIRECTIONS[c]:i for i,c in enumerate(CYCLE)}

def count_value(item:T, array:numpy.ndarray[T]) -> int:
    return (array==item).sum()

@numpy.vectorize
def point_in_cycle(value:int, direction:complex) -> int:
    return CARDINAL.get(direction, value)

vcount_value = numpy.vectorize(count_value, excluded=(1,))


@dataclass(eq=True)
class ElvesGrove:
    positions:numpy.ndarray[complex,complex]

    def __post_init__(self):
        self.positions = numpy.fromiter(self.positions, dtype=complex)
        self._cycle = numpy.zeros_like(self.positions, dtype=int)

    @property
    def measure_ground(self) -> float:
        p = self.positions
        return (1+p.real.max()-p.real.min())*(1+p.imag.max()-p.imag.min()) - len(self)

    def pprint(self, elve=aoc_recipes.BLACK_char, empty=aoc_recipes.WHITE_char ):
        p = self.positions
        x_min, x_max= map(int,(p.real.min(),p.real.max()))
        y_min, y_max= map(int,(p.imag.min(),p.imag.max()))
        for y in range(y_min,1+y_max):
            for x in range(x_min,1+x_max):
                xy = complex(x,y)
                print( elve if xy in p else empty, end="")
            print()

    def __str__(self) -> str:
        p = self.positions
        x_min, x_max= map(int,(p.real.min(),p.real.max()))
        y_min, y_max= map(int,(p.imag.min(),p.imag.max()))
        lines = []
        for y in range(y_min,1+y_max):
            for x in range(x_min,1+x_max):
                xy = complex(x,y)
                lines.append( "#" if xy in p else "." )
        return "\n".join(lines)

    def __len__(self) -> int:
        return len(self.positions)

    def __getitem__(self, index:int|slice) -> complex|numpy.ndarray:
        return self.positions[index]

    def __contains__(self, value) -> bool:
        return value in self.positions

    def elves_take_action(self):
        "said if a given else have any elve adjacent, and thus should take a action in a round"
        @numpy.vectorize
        def have_neigbors(elf:complex) -> bool:
            return len(numpy.intersect1d(nDIRECTIONS + elf, self.positions))>0
        return have_neigbors(self.positions)

    def index(self, elf:complex) -> int:
        return numpy.where(self.positions == elf)[0][0]
    
    def elves_propose_moves(self):
        ""
        @numpy.vectorize
        def pick_direction(elf:complex, cycle_pos:int) -> complex:
            N = len(CYCLE)
            for i in range(N):
                dire = CYCLE[(i+cycle_pos)%N]
                check = CHECK[dire] + elf
                if not len(numpy.intersect1d(check, self.positions)):
                    return DIRECTIONS[dire]
            return 0.0
        return pick_direction(self.positions, self._cycle)

    def round(self) -> bool:
        "one round"
        pos = self.positions
        #first half
        to_move = self.elves_take_action()
        if not to_move.any():
            return False
        direc = self.elves_propose_moves()
        #second half
        temp_pos = pos + (direc*to_move)
        can_move = vcount_value(temp_pos, temp_pos) == 1
        self.positions = pos + (direc*(to_move & can_move))
        self._cycle = (self._cycle +1)%len(CYCLE)
        return True



def main(data:str, rounds = 10) -> int:
    """part 1 of the puzzle """
    play = ElvesGrove(process_data(data))
    for _ in range(rounds):
        play.round()
    return play.measure_ground


def test() -> bool:
    play = ElvesGrove(process_data(test_input))
    for _ in range(10):
        play.round()
    assert str(play) == str( ElvesGrove(process_data(result_test_1))), "no es igual al test result state"
    return play.measure_ground == 110



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) #4336
    












