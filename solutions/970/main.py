from typing import * 

import math 
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0: 
            return []
        logx = 0 if x == 1 else math.log(bound, x)
        logy = 0 if y == 1 else math.log(bound, y)
        ans = set()
        for i in range(int(logx)+1): 
            for j in range(int(logy)+1): 
                num = math.pow(x, i) + math.pow(y, j)
                if num <= bound:
                    ans.add(int(num))
        return list(ans)
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.powerfulIntegers(2, 1, 10) == [9,2,3,5]
    # assert s.powerfulIntegers(2, 3, 10) == [2,3,4,5,7,9,10]