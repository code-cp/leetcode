from typing import * 

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0 
        left, right = 0, 1 
        while left < n-1:  
            while right < n and (right <= left or nums[right] - nums[left] < k): 
                right += 1
            if right < n and left < n and nums[right] - nums[left] == k: 
                res += 1 
            while left < n-1 and nums[left] == nums[left+1]: 
                left += 1 
            left += 1 
        return res 


if __name__ == "__main__":
    s = Solution()

    nums = [1,1,1,2,2]
    k = 0
    assert s.findPairs(nums, k) == 2 

    nums = [1,1,1,1,1]
    k = 0
    assert s.findPairs(nums, k) == 1 

    nums = [1,3,1,5,4]
    k = 0
    assert s.findPairs(nums, k) == 1 

    nums = [3,1,4,1,5]
    k = 2
    assert s.findPairs(nums, k) == 2 