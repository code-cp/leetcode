from typing import * 

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0 

        if n % 2 == 0: 
            pre_even = [0] * (n//2+1)
            pre_odd = [0] * (n//2+1)
        else: 
            # if n is odd, there are n//2+1 even indices 
            pre_even = [0] * (n//2+2)
            # NOTE not n//2+2
            pre_odd = [0] * (n//2+1)

        for i in range(n): 
            if i % 2 == 0: 
                pre_even[i//2+1] = pre_even[i//2]+nums[i]
            else: 
                pre_odd[i//2+1] = pre_odd[i//2]+nums[i]

        for i in range(n): 
            if i % 2 == 0: 
                even = pre_even[i//2] + pre_odd[-1] - pre_odd[i//2]
                odd = pre_odd[i//2] + pre_even[-1] - pre_even[i//2+1]
            else: 
                even = pre_even[i//2+1] + pre_odd[-1] - pre_odd[i//2+1]
                odd = pre_odd[i//2] + pre_even[-1] - pre_even[i//2+1]
            if even == odd: 
                res += 1 

        return res 

if __name__ == "__main__": 
    s = Solution() 

    nums = [1,1,1,1,1]
    assert s.waysToMakeFair(nums) == 5

    nums = [1,1,1]
    assert s.waysToMakeFair(nums) == 3

    nums = [2,1,6,4]
    assert s.waysToMakeFair(nums) == 1