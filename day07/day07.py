#https://adventofcode.com/2022/day/7
#from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
import re
from collections.abc import MutableSequence
import collections

test_input="""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class File:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"{type(self).__name__}({self.size!r}, {self.name!r})"

    def __str__(self):
        return f"{self.name} (file, size={self.size})"

class Folder(collections.UserList):
    
    def __init__(self, name, content=()):
        self.name = name
        super().__init__(content)

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r}, {self.data!r})"

    @property
    def size(self):
        return sum( x.size for x in self )

    def pprint(self, ident:int=0):
        print(" "*ident,"-", self.name, f"(dir, size={self.size})")
        ident+=2
        for x in self:
            if isinstance(x, type(self)):
                x.pprint(ident)
            elif isinstance(x, File):
                print(" "*ident,"-", x)
            else:
                print(" "*ident,"UNKNOW TYPE",repr(x))



def process_data(data:str) -> Iterator[tuple[str,...]]:
    """ """
    yield from ir.isplit(data.strip().replace("$","$$$\n$").splitlines(),lambda x:"$$$" in x)
    return
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def ls_command(data:list[str]):
    def make(item:str):
        kind, name = item.split()
        if kind=="dir":
            return Folder(name)
        if kind.isnumeric():
            return File(kind, name)
        raise ValueError(f"unexpected item: {item!r}")
        
    return [make(x) for x in data]

def build_folder_tree(data, current_folder:Folder=None):
    iter_data = iter(data)
    while True:
        try:
            command, *data = next(iter_data)
        except StopIteration:
            return current_folder
        if command == "$ cd /":
            if current_folder is None:
                current_folder = Folder("/")
            continue
        if command == "$ ls":
            current_folder.extend(ls_command(data))
            continue
        if command == "$ cd ..":
            return current_folder
        if command.startswith("$ cd"):
            _,_,name = command.split()
            next_folder = next( f for f in current_folder if isinstance(f,Folder) and f.name == name)
            build_folder_tree(iter_data, next_folder)
    
            
def walk(folder:Folder):
    yield folder
    for x in folder:
        if isinstance(x,Folder):
            yield from walk(x)

def part1(data:str) -> int:
    """part 1 of the puzzle """
    root = build_folder_tree(process_data(data))
    return sum( f.size for f in walk(root) if f.size<=100_000 )
    
    

def part2(data:str) -> None:
    """part 2 of the puzzle """
    root  = build_folder_tree(process_data(data))
    total = 70000000
    unused = total - root.size
    need  = 30000000
    candidatos = sorted(walk(root),key=lambda f:f.size)
    #print([c.size for c in candidatos])
    for folder in candidatos:
        free = folder.size
        if need < (unused + free):
            return free
            
    
   
def test1() -> bool:
    return 95437 == part1(test_input)

def test2() -> bool:
    return 24933642 == part2(test_input)



#root=build_folder_tree(process_data(test_input))
#root.pprint()



data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) #1206825
assert test2(),"fail test 2"
print("solution part2", part2(data)) #9608311














