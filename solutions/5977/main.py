from typing import List 

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        winSize = sum(nums)
        if winSize == 0:
            return 0
        nums = nums + nums
        minSwap = float("inf")
        curSwap = 0
        for i in range(n+winSize):
            if i < winSize-1:
                if nums[i] == 0:
                    curSwap += 1
            else:
                if nums[i] == 0:
                    curSwap += 1
                if curSwap < minSwap:
                    minSwap = curSwap
                if nums[i+1-winSize] == 0:
                    curSwap -= 1
        return minSwap

if __name__ == "__main__": 
    nums = [0,1,0,1,1,0,0]
    s = Solution()
    assert s.minSwaps(nums) == 1
