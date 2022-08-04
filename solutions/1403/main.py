from typing import * 

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        res = []
        for i, n in enumerate(nums):
            res.append(n) 
            if sum(res) > sum(nums[i+1:]):
                return res 

if __name__ == "__main__": 
    s = Solution()

    nums = [4,3,10,9,8]
    assert s.minSubsequence(nums) == [10,9] 