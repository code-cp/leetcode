# ref 
# https://leetcode.cn/circle/discuss/Kclgr5/view/MEVwaD/
# https://leetcode.cn/problems/minimum-cost-to-split-an-array/solutions/2072764/by-tsreaper-gepe/

# - dp?
# - dfs
# - binary search? 

from typing import * 

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(1, n+1): 
            count = [0]*n   
            t = 0 
            for j in range(i-1, -1, -1): 
                count[nums[j]] += 1 
                c = count[nums[j]]
                if c == 2:
                    t += 2 
                elif c > 2:
                    t += 1  
                dp[i] = min(dp[i], dp[j] + t + k)
        return dp[-1]


if __name__ == "__main__": 
    s = Solution() 

    nums = [1,2,1,2,1,3,3]
    k = 2
    assert s.minCost(nums, k) == 8 

    nums = [1,2,1,2,1]
    k = 2
    assert s.minCost(nums, k) == 6 

    nums = [1,2,1,2,1]
    k = 5
    assert s.minCost(nums, k) == 10 