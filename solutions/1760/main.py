from typing import * 

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def calBag(max_cap): 
            res = 0 
            for n in nums: 
                if n > max_cap: 
                    res += n // max_cap 
                    if n % max_cap > 0: 
                        res += 1 
                else: 
                    res += 1 
            return res 

        n = maxOperations+len(nums)

        # find first min size such that no. bags <= n 
        l, r = 1, max(nums) 
        while l <= r: 
            mid = (r-l)//2+l 
            if calBag(mid) > n: 
                l = mid+1 
            elif calBag(mid) <= n: 
                r = mid-1 

        return int(l) 
        

if __name__ == "__main__": 
    s = Solution() 

    nums = [2,4,8,2]
    maxOperations = 4
    assert s.minimumSize(nums, maxOperations) == 2 

        