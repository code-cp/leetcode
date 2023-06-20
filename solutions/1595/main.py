from typing import * 

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        # dp[i][state] means 0-i nodes in set A, match to state in set B 
        dp = [[float("inf")]*(1<<n) for _ in range(m+1)]
        
        # since index has i-1, need to insert 1 row 
        cost.insert(0, [0]*n)
        dp[0][0] = 0 
        
        cost_subset = [[0]*(1<<n) for _ in range(m+1)]
        for i in range(1,m+1): 
            for state in range(1<<n): 
                total = 0 
                for j in range(n): 
                    if (state >> j) & 1 == 1:
                        total += cost[i][j]
                cost_subset[i][state] = total 
        
        for i in range(1,m+1): 
            for state in range(1<<n): 
                subset = state 
                while subset > 0:
                    dp[i][state] = min(dp[i][state], dp[i-1][state-subset] + cost_subset[i][subset])
                    subset = (subset-1)&state 
                # ref https://www.youtube.com/live/vVOOh0VGiMk?feature=share&t=1282
                mi = float("inf")
                for j in range(n):
                    # NOTE, we choose the min value already in state 
                    if (state>>j) & 1 != 1: 
                        continue  
                    mi = min(mi, cost[i][j])
                dp[i][state] = min(dp[i][state], dp[i-1][state]+mi)
                
        return dp[-1][-1]
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.connectTwoGroups([[15, 96], [36, 2]]) == 17 