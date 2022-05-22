from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        # check input
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        # dp table 1, consider start, do not consider end
        dp1 = [0] * (len(nums)-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
        # dp table 2, consider end, do not consider start
        dp2 = [0] * (len(nums)-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            dp2[i] = max(dp2[i-2] + nums[i+1], dp2[i-1])
        return max(dp1[-1], dp2[-1])

if __name__ == "__main__":
    nums = [2,3,2]
    s = Solution()
    assert s.rob(nums) == 3
