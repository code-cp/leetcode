from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxRange = 0
        i = 0
        while i <= maxRange and i < len(nums):
            maxRange = max(maxRange, nums[i]+i)
            i += 1
        return maxRange >= len(nums)-1

if __name__ == "__main__":
    mySol = Solution()
    nums = [2,3,1,1,4]
    assert mySol.canJump(nums)
