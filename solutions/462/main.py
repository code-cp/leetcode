from typing import * 

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def median(nums):
            if len(nums) % 2 == 0:
                return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2 
            else: 
                return nums[len(nums) // 2] 
        nums = sorted(nums) 
        m = median(nums) 
        return int(sum(abs(n - m) for n in nums)) 

if __name__ == "__main__": 
    s = Solution() 

    nums = [1,0,0,8,6]
    assert s.minMoves2(nums) == 14 