from typing import * 

from collections import defaultdict, Counter  
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        def cntNum(num, count): 
            m = 0 
            while num > 0: 
                if (num & 1) == 1:
                    count[m] += 1 
                num >>= 1 
                m += 1 
        
        n = len(nums)
        count = [[0]*20 for _ in range(n+1)] 
        for i in range(n):
            for j in range(20): 
                count[i+1][j] = count[i][j]
            cntNum(nums[i], count[i+1])
            
        res = 0 
        for i in range(n+1): 
            for j in range(i+1, n+1): 
                valid = True 
                for k in range(20): 
                    if (count[j][k] - count[i][k]) % 2 == 1:  
                        valid = False  
                        break 
                if valid:
                    res += 1 
                
        return res 
        
if __name__ == "__main__": 
    s = Solution() 
    
    nums = [4,3,1,2,4]
    assert s.beautifulSubarrays(nums) == 2 