from typing import * 

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if nums[n//2] != nums[n//2+1]:
            return nums[n//2-1]
        else:
            return nums[len(nums)//2]


if __name__ == "__main__": 
    s = Solution()

    assert s.repeatedNTimes([5,1,5,2,5,3,5,4]) == 5 
    assert s.repeatedNTimes([9,5,3,3]) == 3