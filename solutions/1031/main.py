from typing import * 

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n): 
            prefix[i+1] = prefix[i]+nums[i]
        
        ans = 0 
        for i in range(n-firstLen+1): 
            sum1 = prefix[i+firstLen]-prefix[i]
            for j in range(i-secondLen+1): 
                sum2 = prefix[j+secondLen]-prefix[j]
                ans = max(ans, sum1+sum2)
                pass 
            for j in range(i+firstLen, n-secondLen+1):
                sum2 = prefix[j+secondLen]-prefix[j]
                ans = max(ans, sum1+sum2) 
                pass 
            
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2) == 20 
                     