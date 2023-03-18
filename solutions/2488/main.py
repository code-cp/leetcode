from typing import * 

# key takeaway:
# how to handle index when using prefix 
# need to use i+1 instead of i 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        for i, n in enumerate(nums): 
            if n < k: 
                nums[i] = -1 
            elif n == k: 
                nums[i] = 0 
            else: 
                nums[i] = 1 
                
        # sum of odd len subarray when k is median = 0  
        # sum of even len subarray when k is median = 1 
        # subarray sum -> prefix sum 
        n = len(nums)
        prefix = [0] * (n+1) 
        # how many prefix whose sum == s and len is even
        # NOTE, remember to initialize prefix_even
        prefix_even = {0: 1}
        # how many prefix whose sum == s and len is odd  
        prefix_odd = {}
        
        res = 0 
        for i, num in enumerate(nums): 
            prefix[i+1] = prefix[i] + num 
            if (i+1) % 2 == 0: 
                res += prefix_even.get(prefix[i+1]-1, 0)
                res += prefix_odd.get(prefix[i+1], 0)
                prefix_even[prefix[i+1]] = prefix_even.get(prefix[i+1], 0) + 1 
            else: 
                res += prefix_even.get(prefix[i+1], 0)
                res += prefix_odd.get(prefix[i+1]-1, 0)
                prefix_odd[prefix[i+1]] = prefix_odd.get(prefix[i+1], 0) + 1  
                
        return res 
        
        
if __name__ == "__main__": 
    s = Solution() 
    
    nums = [3,2,1,4,5]
    k = 4
    assert s.countSubarrays(nums, k) == 3 