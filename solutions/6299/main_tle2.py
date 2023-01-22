from typing import * 

from collections import Counter  
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        def countLen(cnt): 
            res = 0 
            for k, v in cnt.items():
                if v > 1: 
                    res += v 
            return res 

        n = len(nums)
        memo = [[0]*n for _ in range(n)]
        for i in range(n): 
            for j in range(i, n): 
                memo[i][j] = k + countLen(Counter(nums[i:j+1]))

        table = {}
        def dfs(memo, pre, cur, res):
            if cur == n:
                pre = min(pre, n-1)
                cur = min(cur, n-1)
                res += memo[pre][cur]
                table[(pre, cur)] = res 
                return res 
            if table.get((pre, cur), -1) != -1: 
                return table[(pre, cur)] 
            opt1 = dfs(memo, pre, cur+1, res)
            opt2 = memo[pre][cur] + dfs(memo, cur+1, cur+1, res)
            res += min(opt1, opt2)
            table[(pre, cur)] = res 
            return res 

        res = dfs(memo, 0, 0, 0)
        return res 

if __name__ == "__main__": 
    s = Solution() 

    # nums = [1,2,1,2,1,3,3]
    # k = 2
    # assert s.minCost(nums, k) == 8 

    # nums = [1,2,1,2,1]
    # k = 2
    # assert s.minCost(nums, k) == 6 

    nums = [1,2,1,2,1]
    k = 5
    assert s.minCost(nums, k) == 10 