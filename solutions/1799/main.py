from typing import * 

class Solution:
    @staticmethod
    def gcd(a, b): 
        while b: 
            a, b = b, a%b 
        return a 

    def dfs(self, nums, opt, mask): 
        # mask: 0 unused, 1 used
        n = len(nums)
        ans = 0 
        if mask == (1 << n - 1): 
            return ans  
        if self.memo[mask] > 0: 
            return self.memo[mask]
        for i in range(n): 
            if mask & (1 << i) == 0: 
                for j in range(i+1, n): 
                    if mask & (1 << j) == 0: 
                        ans = max(ans, opt * self.gcd(nums[i], nums[j]) + self.dfs(nums, opt+1, mask | (1<<i) | (1<<j)))
                        self.memo[mask] = ans 
        return ans 

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo = [0] * (1<<n)
        self.dfs(nums, 1, 0)
        return self.memo[0]

if __name__ == "__main__": 
    s = Solution() 

    nums = [3,4,6,8]
    assert s.maxScore(nums) == 11 