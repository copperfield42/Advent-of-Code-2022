#https://adventofcode.com/2022/day/16
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import prepare_data, prepare_dfs


def main(data:str, show=False) -> int:
    """part 1 of the puzzle """
    #https://www.youtube.com/watch?v=bLMj50cpOug    
    dfs_data = prepare_data(data, show)
    dfs = prepare_dfs(*dfs_data)
    result = dfs(30,"AA")
    if show:
        print("dfs chache info", dfs.cache_info())
    return result    
    


def test() -> bool:
    return main(test_input) == 1651



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












