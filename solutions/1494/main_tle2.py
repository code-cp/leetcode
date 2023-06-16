from typing import * 

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # dp[state] means the min. semester needed to finish state 
        # to transit from pre_state to state 
        # pre_state is a subset of state, since the finished courses should persist
        # the new courses taken <= k 
        # pre_state must contain prerequisites of state 
        # dp[state] = min(dp[state], dp[pre_state]+1)
        
        dp = [float("inf")]*(1<<n)
        # pre_courses[i] means the prerequisites of course i 
        pre_courses = [0]*n 
        
        for r in relations: 
            pre_courses[r[1]-1] += 1<<(r[0]-1)
        
        prerequisites = [0]*(1<<n) 
        
        def countOne(num): 
            cnt = 0 
            while num > 0: 
                num = (num-1)&num 
                cnt += 1 
            return cnt 

        for state in range(1<<n): 
            for i in range(n):
                if (state >> i) & 1 == 0: 
                    continue  
                prerequisites[state] |= pre_courses[i]     
            if prerequisites[state] == 0 and countOne(state) <= k: 
                dp[state] = 1 
        
        dp[0] = 0 
        for state in range(1<<n):
            if dp[state] == 1: 
                continue 
            subset = state 
            while subset > 0: 
                subset = (subset-1)&state
                if countOne(state) - countOne(subset) > k: 
                    continue 
                if subset & prerequisites[state] != prerequisites[state]: 
                    continue 
                dp[state] = min(dp[state], dp[subset]+1)
                
        return dp[(1<<n) - 1]

if __name__ == "__main__": 
    s = Solution()
    
    assert s.minNumberOfSemesters(4, [[2,1],[3,1],[1,4]], 2) == 3 