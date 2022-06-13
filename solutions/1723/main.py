from typing import * 

# TLE，为啥？？
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        state2time = lambda state: sum(jobs[i] for i, j in enumerate(jobs) if state & (1 << i)) 
        # init dp table 
        n = len(jobs)
        dp = [[0] * (2 ** n) for _ in range(k)]
        for state in range(2 ** n): 
            dp[0][state] = state2time(state) 
        # traverse 
        for i in range(1, k):
            for state in range(2**n): 
                substate = state 
                min_c = float('inf') 
                while substate > 0:  
                    min_c = min(min_c, max(dp[i-1][state^substate], dp[0][substate]))
                    substate = (substate - 1) & state 
                dp[i][state] = min_c 
        return dp[-1][-1] 


if __name__ == "__main__": 
    s = Solution() 

    jobs = [3,2,3]
    k = 3
    assert s.minimumTimeRequired(jobs, k) == 3 

    jobs = [20010,20006,20014,20004,20008,20006,20005,20012,19999,20014,20003,20012]
    k = 8
    assert s.minimumTimeRequired(jobs, k) == 40011