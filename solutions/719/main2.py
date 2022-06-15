from typing import * 

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(nums, max_diff): 
            n = len(nums) 
            dp = [0] * n  
            r = 1 
            for l in range(0, n): 
                while r < n: 
                    diff = nums[r] - nums[l] 
                    if diff > max_diff:
                        break 
                    r += 1 
                if l == 0: 
                    dp[l] = r - l - 1  
                else:
                    dp[l] = dp[l-1] + r - l - 1 
            return dp[-2]
            
        def bsearch(nums, l, r, target): 
            while l <= r: 
                m = (r - l) // 2 + l 
                if count(nums, m) < target: 
                    l = m + 1
                elif count(nums, m) >= target:
                    r = m - 1 
            return l
        nums.sort()
        l = min([nums[i] - nums[i-1] for i, _ in enumerate(nums) if i > 0])
        r = nums[-1] - nums[0]
        m = bsearch(nums, l, r, k)
        return m 

if __name__ == "__main__": 
    s = Solution()

    assert s.smallestDistancePair([1,3,1], 1) == 0

    assert s.smallestDistancePair([1,1,1], 2) == 0

    assert s.smallestDistancePair([1,6,1], 3) == 5

    assert s.smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18) == 2