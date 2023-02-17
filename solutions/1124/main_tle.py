from typing import * 

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        tiring = [0]*n 
        for i in range(n): 
            if hours[i] > 8: 
                tiring[i] = 1
            else: 
                tiring[i] = -1 

        pre = [0]*(n+1)
        for i in range(1, n+1): 
            pre[i] = pre[i-1] + tiring[i-1]

        res = 0 
        for i in range(1, n+1): 
            if tiring[i-1] > 0: 
                res = max(1, res)
            for j in range(i): 
                if pre[i] - pre[j] > 0: 
                    res = max(res, i-j)
                    break 

        return res 


if __name__ == "__main__": 
    s = Solution() 
    
    hours = [9,9,6,0,6,6,9]
    assert s.longestWPI(hours) == 3 