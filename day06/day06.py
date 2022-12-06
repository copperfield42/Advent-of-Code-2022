#https://adventofcode.com/2022/day/6
#from __future__ import annotations


from typing import Iterator
import itertools_recipes as ir


test_input_list="""mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""".split()

def process_data(data:str, size:int) -> int:
    """said how many character need so you get size consecutives distint characters   """
    for group in ir.groupwise(enumerate(data,1),size):
        chars = { c for i,c in group }
        if len(chars)==size:
            return group[-1][0]
    raise ValueError(f"no windows of {size=} detected")
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



def part1(data:str) -> int:
    """part 1 of the puzzle """
    return process_data(data,4)

def part2(data:str) -> None:
    """part 2 of the puzzle """
    return process_data(data,14)
   
def test1():
    pass_test=True
    for n,(test,expected) in enumerate( zip(test_input_list,[7,5,6,10,11]),1):
        got = part1(test)
        if got != expected:
            print(f"fail test {n}, {expected=} {got=}\nwith input={test!r}\n")
            pass_test=False
    if pass_test:
        print("pass all test cases of part 1")
    return pass_test

def test2():
    pass_test=True
    for n,(test,expected) in enumerate( zip(test_input_list,[19,23,23,29,26]),1):
        got = part2(test)
        if got != expected:
            print(f"fail test {n}, {expected=} {got=}\nwith input={test!r}\n")
            pass_test=False
    if pass_test:
        print("pass all test cases of part 2")
    return pass_test



assert test1(),"fail test 1"
assert test2(),"fail test 2"
#""
data = get_raw_data()
print("solution part1", part1(data))
print("solution part2", part2(data))
#"""













