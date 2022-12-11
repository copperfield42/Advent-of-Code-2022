#https://adventofcode.com/2022/day/11
#from __future__ import annotations

from typing import Iterator, Callable
import itertools_recipes as ir
from functools import partial
import operator
import re
from dataclasses import dataclass, field
from collections import Counter
from math import prod



test_input="""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

def make_operation(text:str) -> Callable[[int],int]:
    def fun1(x,fun):
        return fun(x,x)
    for char,op in zip("+*",[operator.add, operator.mul]):
        if char in text:
            x,y = map(str.strip, text.split(char))
            if x==y:
                return partial(fun1,fun=op)
            return partial(op,int(y))
    raise ValueError(f"Unexpedted token: {text!r}")


@dataclass
class Monkey:
    m_id:int
    items:list[int]
    operation:Callable[[int],int]
    test:int
    t_true:int
    t_false:int

    @classmethod
    def from_strs(cls, m_id, items, operation, test, t_true, t_false):
        args = [
            int(re.match("Monkey (\d+):", m_id).groups()[0]),
            list(map(int,items.split(":")[-1].split(","))),
            make_operation(operation.split("=")[-1]),
            int(test.split()[-1]),
            int(t_true.split()[-1]),
            int(t_false.split()[-1]),
            ]
        return cls(*args)
            
@dataclass    
class Game:
    monkeys:list[Monkey]
    inspect:dict[int,int] = field(default_factory=Counter, init=False)
    worry_divider:Callable[[int],int] = lambda x:x//3


    def turn(self, monkey_id):
        monkeys = self.monkeys
        monkey = monkeys[monkey_id]
        worry_divider = self.worry_divider
        test = monkey.test
        t_true = monkeys[monkey.t_true].items.append
        t_false = monkeys[monkey.t_false].items.append
        inspect = self.inspect
        operation = monkey.operation
        for worry_level in monkey.items:
            new = worry_divider( operation(worry_level) )
            if new%test == 0:
                t_true(new)
            else:
                t_false(new)
            inspect[monkey_id] += 1
        monkey.items.clear()

    def round(self):
        for n in range(len(self.monkeys)):
            self.turn(n)

    def play(self, n_round:int):
        for _ in range(n_round):
            self.round()

    def monkey_business(self, n_monkey:int) -> int:
        return prod( v for _,v in self.inspect.most_common(n_monkey))
        pass
        
           

    def pprint(self):
        for m in self.monkeys:
            print(m)
            print()
            
            

def process_data(data:str) -> Iterator[Monkey]:
    """transform the raw data into a procesable form"""
    for monkey in ir.isplit(data.splitlines()):
        yield Monkey.from_strs(*map(str.strip, monkey))
    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def part1(data:str) -> int:
    """part 1 of the puzzle """
    game = Game(list(process_data(data)))
    game.play(20)
    return game.monkey_business(2)


def part2(data:str, on:str="#", off:str="." ) -> str:
    """part 2 of the puzzle """
    game = Game(list(process_data(data)))
    mod = prod( m.test for m in game.monkeys )
    game.worry_divider = lambda x : x%mod
    game.play(10000)
    return game.monkey_business(2)
     
    
 
    
   
def test1() -> bool:
    return part1(test_input) == 10605

def test2() -> bool:
    return part2(test_input) == 2713310158



data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1:", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2:", part2(data)) #














