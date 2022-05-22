from typing import * 

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        score_acu = [0] * n 
        for i in range(n): 
            # move to right end 
            good = (i+1)%n
            # move to invalid region 
            bad = (good + n - nums[i])%n 
            score_acu[good] += 1 
            score_acu[bad] -= 1
            if bad > good: 
                score_acu[0] -= 1 

        ans = 0
        max_score = -float("inf")
        cur_sum = 0 
        for i in range(n):
            cur_sum += score_acu[i] 
            if cur_sum > max_score: 
                max_score = cur_sum
                ans = i 
        
        return ans 

if __name__ == "__main__": 
    s = Solution()

    nums = [2,3,1,4,0]
    result = s.bestRotation(nums)
    assert result == 3 