from typing import List 

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i] 
        return result 

if __name__ == "__main__": 
    nums = [3,3,7,7,10,11,11]
    s = Solution()
    assert s.singleNonDuplicate(nums) == 10