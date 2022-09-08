from typing import * 

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1: 
            return list(range(1, n+1))
        res = []
        i, j = 1, n
        while i < j and k > 0: 
            res.append(i)
            i += 1 
            k -= 1 
            if k <= 0: 
                while i <= j:
                    res.append(i)
                    i += 1  
                break 
            res.append(j)
            j -= 1 
            k -= 1 
            if k <= 0:
                while j >= i:
                    res.append(j)
                    j -= 1   
                break 
        return res  


if __name__ == "__main__": 
    s = Solution()

    n = 3
    k = 1
    assert s.constructArray(n, k) == [1,2,3]


    n = 3
    k = 2
    assert s.constructArray(n, k) == [1,3,2]

