from curses.ascii import SO
from typing import List 

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float("inf")
        for i in range(len(nums)): 
            if i >= k-1: 
                min_diff = min(nums[i] - nums[i-k+1], min_diff)
        return min_diff

if __name__ == "__main__": 
    s = Solution()
    nums = [9,4,1,7]
    k = 2
    assert s.minimumDifference(nums, k) == 2