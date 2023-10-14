from typing import * 

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n): 
            if s[i] == "L": 
                nums[i] -= d 
            else: 
                nums[i] += d 
        
        res = 0 
        M = 10**9 + 7 
        nums.sort()
        # print(f"{nums=}")
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            total = (i * (n-i)) * diff
            res += total % M 
            res %= M 
            
        return res  

if __name__ == "__main__": 
    s = Solution()
    
    assert s.sumDistance([-2,0,2], "RLL", 3) == 8