from typing import List 

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        if k % 2:
            nums[-1] *= -1
        result = 0
        for i in range(len(nums)):
            result += nums[i]
        return result

if __name__ == "__main__":
    nums = [4,2,3]
    k = 1 
    mySol = Solution()
    assert mySol.largestSumAfterKNegations(nums, k) == 5
