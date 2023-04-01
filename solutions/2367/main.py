from typing import * 
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        # dp[i] means how many pairs that end at i 
        dp = [0]*n
        hashmap = {}
        for i in range(n):
            num = nums[i]-diff 
            if num in hashmap: 
                j = hashmap[num]
                dp[i] = dp[j]+1 
                # remove duplicates 
                dp[j] = 0
            hashmap[nums[i]] = i
        res = 0 
        for i in range(n): 
            if dp[i] >= 2: 
                res += dp[i]-1
        return res 
    
if __name__ == "__main__": 
    s = Solution() 
    
    nums = [0,1,4,6,7,10]
    diff = 3
    assert s.arithmeticTriplets(nums, diff) == 2 
            

            
        