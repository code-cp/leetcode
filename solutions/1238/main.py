from typing import * 

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        # 0th gray code 
        res.append(0)
        
        for i in range(n): 
            l = len(res)
            # generate ith gray code  
            for j in range(l-1, -1, -1): 
                res.append(res[j] + (1<<i))
        
        while res[0] != start: 
            res.append(res[0])
            del res[0]

        return res 

if __name__ == "__main__": 
    s = Solution() 

    assert s.circularPermutation(2, 3) == [3,2,0,1]