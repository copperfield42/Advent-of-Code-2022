#https://adventofcode.com/2022/day/16
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import prepare_data, prepare_dfs
from aoc_recipes import progress_bar




def main(data:str,show=False) -> int:
    """part 2 of the puzzle """
    #https://www.youtube.com/watch?v=bLMj50cpOug    
    dfs_data = prepare_data(data, show)
    dfs = prepare_dfs(*dfs_data)
    total = (1<<len(dfs_data[1]))-1
    result = max( dfs(26,"AA",i)+dfs(26,"AA",total^i) for i in progress_bar(range( (total+1)//2 )))
    if show:
        print("dfs chache info", dfs.cache_info())
    return result



def test() -> bool:
    return main(test_input) == 1707



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













