from typing import * 

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        calBag = lambda max_cap: sum([(n-1)//max_cap for n in nums])

        # find first min size such that no. bags <= n 
        l, r = 1, max(nums) 
        while l <= r: 
            mid = (r-l)//2+l 
            ops = calBag(mid)
            if ops > maxOperations: 
                l = mid+1 
            elif ops <= maxOperations: 
                r = mid-1 

        return int(l) 
        

if __name__ == "__main__": 
    s = Solution() 

    nums = [2,4,8,2]
    maxOperations = 4
    assert s.minimumSize(nums, maxOperations) == 2 

        