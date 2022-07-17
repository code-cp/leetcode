from typing import * 

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        total = len(nums)
        left = total 
        nums.sort()
        ans = [0, 0]
        i = 1 
        while i < total: 
            if nums[i] == nums[i-1]:
                ans[0] += 1 
                left -= 2 
                i += 1 
            i += 1 
        ans[1] = left 
        return ans 

if __name__ == "__main__": 
    s = Solution()

    nums = [1,3,2,1,3,2,2]
    assert s.numberOfPairs(nums) == [3,1]