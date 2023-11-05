from typing import * 

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # All elements in nums are distinct
        
        n = len(nums)
        prod_map = {}
        for i in range(n): 
            for j in range(i+1, n): 
                prod = nums[i] * nums[j]
                if prod not in prod_map:
                    prod_map[prod] = 1
                else:
                    prod_map[prod] += 1
        
        ans = 0 
        for _, v in prod_map.items(): 
            if v == 1:
                continue 
            ans += v*(v-1)//2 * 8 
                    
        return ans 
                
if __name__ == "__main__": 
    s = Solution()
    
    assert s.tupleSameProduct([2,3,4,6]) == 8  
        