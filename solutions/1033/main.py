from typing import * 

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        min_move = 2        
        a,b,c = sorted([a,b,c])
        if c-a==2:
            min_move = 0 
        elif b-a==1 or c-b==1: 
            min_move = 1
        elif b-a==2 or c-b==2: 
            min_move = 1 
        max_move = c-b-1+b-a-1  
        return [min_move,max_move]
        
if __name__ == "__main__": 
    s = Solution() 

    assert s.numMovesStones(3,5,1) == [1,2]
    assert s.numMovesStones(4,3,2) == [0,0]  
    assert s.numMovesStones(1,2,5) == [1,2]
             
            