from typing import * 

from collections import defaultdict 
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def num2sum(num):
            ans = 0 
            while num > 0: 
                ans += num % 10 
                num //= 10 
            return ans  
        ans = -1 
        dt = defaultdict(int)
        for i, n in enumerate(nums): 
            key = num2sum(n)
            if key not in dt:
                dt[key] = n 
                continue 
            ans = max(dt[key] + n, ans)
            dt[key] = max(dt[key], n)
        return ans 

if __name__ == "__main__": 
    s = Solution()

    nums = [18,43,36,13,7]
    assert s.maximumSum(nums) == 54

    nums = [10,12,19,14]
    assert s.maximumSum(nums) == -1