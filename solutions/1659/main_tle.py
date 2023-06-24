from typing import * 
import math 
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
            # dp[i][state] = max. value if you arrange ith row as state 
            # but we also need to make sure total intro and extro are within limits 
            # so dp[i][x][y][state]: max. value if arrange ith row as state with x intro, y extro 
            
            inf = float("inf")
            dim1 = 6
            dim2 = 7 
            dim3 = 7 
            dim4 = 3**5 
            dp = [[[[-inf for _ in range(dim4)] for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
            max_state = 3**n
            ans = 0 
                        
            dp[0][0][0][0] = 0
            
            def countPeople(state):
                nonlocal n 
                count1 = count2 = 0 
                for i in range(n): 
                    r = state % 3 
                    if r == 1: 
                        count1 += 1 
                    elif r == 2: 
                        count2 += 1 
                    state //= 3 
                return count1, count2 
            
            def addVal(pre, cur): 
                p = [0]*6 
                q = [0]*6
                
                for i in range(n): 
                    p[i] = pre % 3 
                    pre //= 3 
                    q[i] = cur % 3 
                    cur //= 3 
                
                res = 0 
                for i in range(n): 
                    if q[i] == 1: 
                        res += 120 
                        if i >= 1 and q[i-1] > 0:
                            res -= 30 
                        if i+1 < n and q[i+1] > 0: 
                            res -= 30 
                        if p[i] > 0: 
                            res -= 30 
                            
                        if p[i] == 1: 
                            res -= 30 
                        elif p[i] == 2: 
                            res += 20 
                    elif q[i] == 2: 
                        res += 40 
                        if i > 0 and q[i-1] > 0: 
                            res += 20 
                        if i < n-1 and q[i+1] > 0: 
                            res += 20 
                        if p[i] > 0: 
                            res += 20 
                            
                        if p[i] == 1: 
                            res -= 30 
                        elif p[i] == 2: 
                            res += 20 
                    
                return res 
                        
            # NOTE, row starts at index 1 
            # row 0 is for initialization 
            for i in range(1,m+1): 
                for x in range(introvertsCount+1): 
                    for y in range(extrovertsCount+1): 
                        for state in range(max_state):
                            a, b = countPeople(state)
                            if a > x or b > y: 
                                continue 
                            for pre_state in range(max_state):
                                # in the ref video, INT_MAX/2 is used here, but it should be INT_MIN/2
                                if not math.isfinite(dp[i-1][x-a][y-b][pre_state]):
                                    continue                               
                                dp[i][x][y][state] = max(
                                    dp[i][x][y][state],
                                    dp[i-1][x-a][y-b][pre_state] + addVal(pre_state, state)                     
                                    ) 
                            if i == m: 
                                ans = max(ans, dp[i][x][y][state])

            return ans 
        
if __name__ == "__main__": 
    s = Solution()
    
    assert s.getMaxGridHappiness(2,3,1,2) == 240