from typing import List 

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # greedy approach
        result = 1

        # check input
        if len(nums) == 1:
            return result

        count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1

            if result < count:
                result = count

        return result

if __name__ == "__main__": 
    nums = [1,3,5,4,7]
    s = Solution()
    assert s.findLengthOfLCIS(nums) == 3
