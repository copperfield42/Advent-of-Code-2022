#https://adventofcode.com/2022/day/18
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import make_matrix


from scipy.signal import convolve2d
import numpy

CON1 = numpy.array([[ 0,-1, 0],
                    [-1, 4,-1],
                    [ 0,-1, 0]] )

CON2 = numpy.array([[ 0,-1, 0],
                    [ 0, 2, 0],
                    [ 0,-1, 0]] )

def calculate(matrix:numpy.ndarray[bool,bool,bool]) -> int:
    size = matrix.shape[0]
    total = 0
    for n in range(size):
        #convolve x
        temp =  convolve2d(matrix[n], CON1, mode="same")
        total += temp[temp>0].sum()
        #convolve y
        temp =  convolve2d(matrix[:,n,:], CON2, mode="same")
        total += temp[temp>0].sum()
    return total

def main(data:str) -> int:
    """part 1 of the puzzle """
    matrix = make_matrix(data)
    return calculate(matrix)


def test() -> bool:
    return main(test_input) == 64



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1")
    data = get_raw_data()
    print("solution part1:", main(data)) # 3636
    












