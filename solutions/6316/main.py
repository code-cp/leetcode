from typing import * 

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        prefix = [0]*(n+1)
        score = 0 
        for i in range(1, n+1): 
            prefix[i] = prefix[i-1] + nums[i-1]
            if prefix[i] > 0: 
                score += 1 
            else: 
                return score 
        return score 
        
if __name__ == "__main__": 
    s = Solution() 
    
    nums = [2,-1,0,1,-3,3,-3]
    assert s.maxScore(nums) == 6 