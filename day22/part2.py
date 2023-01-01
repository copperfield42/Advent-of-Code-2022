#https://adventofcode.com/2022/day/22
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import point_score, simulate, MPoint, Callable, DIRECCION
import numpy

def make_move_rule(tablero:numpy.ndarray[int,int]) -> Callable[[MPoint,MPoint,numpy.ndarray[int,int]],MPoint]:
    a = (tablero!=0).sum(axis=0)
    b = (tablero!=0).sum(axis=1)
    region_size = min( a[a>0].min(), b[b>0].min() )
    cube = (tablero!=0)*1
    pos  = MPoint(1,numpy.where(tablero[1]==1)[0].min())
    row = 1
    top = cube.shape[1]+1
    n=11
    points = []
    while 1 in cube:
        try:
            col = numpy.where(cube[row]==1)[0].min(initial=top)
        except IndexError:
            break
        if col == top:
            row += region_size 
            continue
        cube[row:row+region_size, col:col+region_size] = n
        points.append( (row,col) )
        n += 1
        if n>20:
            raise RuntimeError("Malformed tablero")
    print(points)
    return cube
    
        
        
        
        
    
def move_rule_sample(position:Point, direction:Point, tablero:numpy.ndarray[int,int]) -> tuple[Point, Point]:
    """
        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666
        """    
    new = position + direction
    if tablero[new] != 0:
        return new, direction
    row, column = position
    Point = type(position)
    match DIRECCION[direction]:
        case ">":
            match column:
                case 12: 
                    if 0 < row <= 4:#1->6
                        return Point(13-row,16),DIRECCION["<"]
                    elif 4 < row <= 8:#4->6
                        return Point(9,21-row),DIRECCION["v"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case 16:
                    if 8 < row <= 12:#6->1
                        return Point(13-row,12),DIRECCION["<"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")
            pass
        case "v":
            match row:
                case 8:
                    if 0 < column <= 4:#2->5
                        return Point(12,13-column), DIRECCION["^"]
                    elif 4 < column <= 8:#3->5
                        return Point(17-column,9), DIRECCION[">"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case 12:
                    if 8 < column <= 12:#5->2
                        return Point(8,13-column), DIRECCION["^"]
                    elif 12 < column <= 16:#6->2
                        return Point(21-column,1), DIRECCION[">"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")
            pass
        case "<":
            match column:
                case 1:
                    if 4 < row <= 8:#2->6
                        return Point(12,21-row), DIRECCION["^"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case 9:
                    if 0 < row <= 4:#1->3
                        return Point(5,5-row), DIRECCION["v"]
                    elif 8 < row <= 12:#5->3
                        return Point(8,17-row), DIRECCION["^"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")
            pass
        case "^":
            match row:
                case 1:
                    if 8 < column <= 12:#1->2
                        return Point(5,13-column), DIRECCION["v"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")    
                case 5:
                    if 0 < column <= 4:#2 -> 1
                        return Point(1,13-column), DIRECCION["v"]
                    elif 4 < column <= 8:#3 -> 1
                        return Point(column-4,9), DIRECCION[">"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")    
                case 9:
                    if 12 < column <= 16 :#6->4
                        return Point(21-column,12), DIRECCION["<"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")    
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")    
            pass
        case _:
            raise RuntimeError
    raise RuntimeError

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
def move_rule_input(position:Point, direction:Point, tablero:numpy.ndarray[int,int]) -> tuple[Point, Point]:
    """
    50   100  150
     1111122222   1
     1111122222 
     1111122222 
     1111122222 
     1111122222   50
     33333
     33333
     33333
     33333        100
4444455555          
4444455555    
4444455555    
4444455555    
4444455555        150
66666    
66666    
66666    
66666             200
    """
    new = position + direction
    if tablero[new] != 0:
        return new, direction
    row, column = position
    Point = type(position)
    match DIRECCION[direction]:
        case ">":
            match column:
                case 150: 
                    if 0 < row <= 50:# 2 -> 5
                        return Point(151-row,100),DIRECCION["<"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case 100:
                    if 50 < row <= 100:# 3 -> 2
                        return Point(50,50+row),DIRECCION["^"]
                    elif 100 < row <= 150:# 5 -> 2 
                        return Point(151-row,150),DIRECCION["<"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case  50:
                    if 150 < row <= 200: # 6 -> 5
                        return Point(150,row-100),DIRECCION["^"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")
            pass
        case "v":
            match row:
                case 200: 
                    if 0 < column <= 50:# 6 -> 2
                        return Point(1,column+100),DIRECCION["v"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case 150:
                    if 50 < column <= 100:# 5 -> 6
                        return Point(column+100,50),DIRECCION["<"]                       
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case  50:
                    if 100 < column <= 150:#2 -> 3
                        return Point(column-50,100),DIRECCION["<"]                        
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")                
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")        
            pass
        case "<":
            match column:
                case 51: 
                    if 0 < row <= 50:# 1 -> 4
                        return Point(151-row,1),DIRECCION[">"]
                    elif 50 < row <= 100:# 3 -> 4
                        return Point(101,row-50),DIRECCION["v"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case 1:
                    if 100 < row <= 150:# 4 -> 1
                        return Point(151-row,51),DIRECCION[">"]
                    elif 150 < row <= 200: #6 -> 1
                        return Point(1,row-100),DIRECCION["v"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")        
            pass
        case "^":
            match row:
                case 101: 
                    if 0 < column <= 50:# 4 -> 3
                        return Point(column+50,51),DIRECCION[">"]
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case 1:
                    if 50 < column <= 100:# 1 -> 6
                        return Point(column+100,1),DIRECCION[">"]
                    elif 100 < column <= 150:# 2 -> 6
                        return Point(200,column-100),DIRECCION["^"]                        
                    else:
                        raise ValueError(f"invalid position direction pair {position=} {direction=}")
                case _:
                    raise ValueError(f"invalid position direction pair {position=} {direction=}")        
            pass
        case _:
            raise RuntimeError
    raise RuntimeError
    

def main(data:str, rule=move_rule_input, show=False) -> int:
    """part 2 of the puzzle """
    path, tablero = process_data(data)
    return simulate(path, tablero, rule, show=show)




def test() -> bool:
    return main(test_input, move_rule_sample,1) == 5031



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













