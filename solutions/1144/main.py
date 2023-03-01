from typing import * 

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return 0 

        res_even = 0 
        for i in range(0, n, 2): 
            if i == 0: 
                res_even += max(0, nums[i]-nums[i+1]+1)
            elif i == n-1: 
                res_even += max(0, nums[i]-nums[i-1]+1)
            else: 
                res_even += max(max(0, nums[i]-nums[i+1]+1), max(0, nums[i]-nums[i-1]+1))

        res_odd = 0 
        for i in range(1, n, 2): 
            if i == n-1: 
                res_odd += max(0, nums[i]-nums[i-1]+1)
            else: 
                res_odd += max(max(0, nums[i]-nums[i+1]+1), max(0, nums[i]-nums[i-1]+1))

        return min(res_even, res_odd)

if __name__ == "__main__": 
    s = Solution()

    assert s.movesToMakeZigzag([2,7,10,9,8,9]) == 4 
    # assert s.movesToMakeZigzag([1,2,3]) == 2 