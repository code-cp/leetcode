from typing import * 

# tle 
# [2463,5070,8566,657,4774,467,707,7043,5]

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if n == 1: 
            return False 

        # dp[sum][num] = dp[sum-nums[i]][num-1]
        dp = [[False for _ in range(n+1)] for _ in range(total+1)]
        # num = 0, sum = 0 
        dp[0][0] = True 

        cur_sum = 0 
        for i in nums: 
            cur_sum += i 
            # NOTE, need to iterate from large to small 
            for j in range(n//2+1, 0, -1): 
                for k in range(cur_sum, i-1, -1):
                    if dp[k-i][j-1]:
                        dp[k][j] = True 
                        if j != n and total * j == k * n:
                            return True 

        return False 


if __name__ == "__main__": 
    s = Solution() 

    nums = [3,1]
    assert not s.splitArraySameAverage(nums)

