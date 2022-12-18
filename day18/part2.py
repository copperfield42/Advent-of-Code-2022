#https://adventofcode.com/2022/day/18
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import make_matrix
import aoc_recipes
from part1 import calculate 
import itertools_recipes as ir

from scipy.signal import convolve2d
import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import string




def plot(matrix):
    fig = plt.figure()
    ax = fig.add_subplot( projection="3d")
    xs,ys,zs = np.where(matrix)
    ax.scatter(xs,ys,zs, c="r", marker="s")
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    plt.show()
    
def show(matrix):
    size = matrix.shape[0]
    label = string.digits+string.ascii_letters
    for x in range(size):
        print(f"slice {x=}")
        print(label[:size])
        sub = matrix[x]
        for y in range(size):
            for z in range(size):
                print( aoc_recipes.BLACK_char if sub[y,z] else aoc_recipes.WHITE_char, end="")
            print("",y)


def fill_gas(matrix:numpy.ndarray[bool,bool,bool], ini:tuple[int,int,int]=(0,0,0)) -> numpy.ndarray[bool,bool,bool]:
    """return a coordinate matrix of all the point that
       can be reach by gas from the given initial point"""
    result = numpy.zeros(matrix.shape, dtype=bool)
    points = set(ir.product(range(matrix.shape[0]), repeat=3))
    points.difference_update(zip(*numpy.where(matrix)))
    work = {ini}
    while work:
        p = work.pop()
        result[p] = True
        points.discard(p)
        x,y,z = p
        new_p = [(x+1,y,z),
                 (x-1,y,z),
                 (x,y+1,z),
                 (x,y-1,z),
                 (x,y,z+1),
                 (x,y,z-1)]
        new_work = [ np for np in new_p if np in points]
        work.update(new_work)
    return result
        
             

    
def main(data:str, show=False) -> int:
    """part 2 of the puzzle """
    matrix = make_matrix(data)
    gas = fill_gas(matrix)
    return calculate(~gas)


def test() -> bool:
    return main(test_input,1) == 58



if __name__ == "__main__":    
    assert test(),"fail test part 2"
    print("pass test part 2")
    data = get_raw_data()
    print("solution part2:", main(data,1)) # 2102
    













