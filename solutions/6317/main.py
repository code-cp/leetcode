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
        odd_count = [0]*(n+1) 
        # 2 = 10, => odd = 2
        # 3 = 11, => odd = 3 
        # 20020004000010 => odd = 2 
        for i in range(n):
            for j in range(20): 
                count[i+1][j] = count[i][j]
            cntNum(nums[i], count[i+1])
            odd = 0 
            for j in range(20): 
                if count[i+1][j] % 2 == 1: 
                    odd += (1<<j)
            odd_count[i+1] = odd  
        
        res = 0 
        odd_map = {0: 1}
        for i in range(1, n+1): 
            odd_cur = odd_count[i]
            if odd_map.get(odd_cur, -1) != -1: 
                res += odd_map[odd_cur]
            else: 
                odd_map[odd_cur] = 0
            odd_map[odd_cur] += 1 
                
        return res 
        
if __name__ == "__main__": 
    s = Solution() 
    
    nums = [4,3,1,2,4]
    assert s.beautifulSubarrays(nums) == 2 