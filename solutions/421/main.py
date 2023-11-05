from typing import * 

# ref https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/solutions/2511644/tu-jie-jian-ji-gao-xiao-yi-tu-miao-dong-1427d/?envType=daily-question&envId=2023-11-04

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0 
        # bit length is the total length of bits 
        high_bit = max(nums).bit_length() - 1 
        
        for i in range(high_bit, -1, -1): 
            # bits lower than i are set to 0 
            mask |= 1 << i
            # check if current bit can be 1 
            target = ans | (1 << i)
            masked_nums = set([x & mask for x in nums])
            for x in masked_nums: 
                # a xor b = x 
                # then a xor b xor b = x xor b 
                # then a = x xor b
                # equivalent to find x + y = target  
                if target ^ x in masked_nums: 
                    ans = target  
                    break 
        
        return ans 
            
        