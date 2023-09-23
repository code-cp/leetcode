from typing import * 

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def isValid(cap): 
            nonlocal nums
            nonlocal n  
            nonlocal k 
            # dp[i] means in the [0,i] houses, the max capability is cap, 
            # how many houses can be selected 
            dp = [0]*n
            # init  
            dp[0] = 1 if nums[0] <= cap else 0 
            for i in range(1, n): 
                if nums[i] > cap: 
                    dp[i] = dp[i-1]
                else: 
                    # either choose i or do not choose i 
                    dp[i] = max(dp[i-1], dp[i-2]+1)
            if dp[-1] >= k:
                return True 
            else: 
                return False 

        # find the smallest cap value that is valid 
        max_cap = max(nums) 
        l, r = 1, max_cap 
        while l <= r: 
            mid = (r-l)//2 + l 
            if isValid(mid):
                r = mid - 1 
            else: 
                l = mid + 1 
        
        return r + 1  
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.minCapability([2,3,5,9], 2) == 5                     
    # assert s.minCapability([2,7,9,3,1], 2) == 2                    
    # assert s.minCapability([1], 1) == 1
    assert s.minCapability([4,22,11,14,25], 3) == 25   