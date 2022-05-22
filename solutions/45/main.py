from typing import List 

class Solution:
    def jump(self, nums: List[int]) -> int:
        maxRange = 0
        nextRange = 0
        result = 0
        for i in range(len(nums)-1):
            nextRange = max(nextRange, i + nums[i])
            if i == maxRange:
                maxRange = nextRange
                result += 1
        return result

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    mySol = Solution()
    assert mySol.jump(nums) == 2
