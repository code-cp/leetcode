from typing import * 

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        tiring = [0]*n 
        res = 0 
        for i in range(n): 
            if hours[i] > 8: 
                tiring[i] = 1
                res = 1 
            else: 
                tiring[i] = -1 

        if res == 0: 
            return 0 

        pre = [0]*(n+1)
        for i in range(1, n+1): 
            pre[i] = pre[i-1] + tiring[i-1]

        m = {}
        for i in range(n+1): 
            if m.get(pre[i], -1) == -1: 
                m[pre[i]] = i 
            if pre[i] > 0: 
                res = max(res, i)
            else: 
                j = m.get(pre[i]-1, -1)
                if j != -1:   
                    # NOTE i-j not i-j+1 since we are using prefix sum 
                    res = max(res, i-j)

        return res 


if __name__ == "__main__": 
    s = Solution() 
    
    hours = [9,9,6,0,6,6,9]
    assert s.longestWPI(hours) == 3 