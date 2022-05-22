from typing import List 

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        preDiff = 0
        curDiff = 0
        result = 1
        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1
                preDiff = curDiff
        return result

if __name__ == "__main__":
    nums = [1,7,4,9,2,5]
    mySol = Solution()
    assert mySol.wiggleMaxLength(nums) == 6
