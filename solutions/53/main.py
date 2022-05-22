from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if result < temp:
                result = temp
            if temp <= 0:
                temp = 0
        return result

if __name__ == "__main__":
    mySol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4];
    assert mySol.maxSubArray(nums) == 6
