from typing import * 

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if n == 1: 
            return False 
        if total == 0: 
            return True 

        # dp[sum] is b00001, means dp[sum][1] = True 
        # dp[sum] |= dp[sum-i] << 1 
        dp = [0 for _ in range(total+1)]
        dp[0] = 1 

        cur_sum = 0 
        for i in nums: 
            cur_sum += i 
            for j in range(cur_sum, i-1, -1):
                # NOTE, iterate from large to small  
                dp[j] |= dp[j-i] << 1 

                if (j*n)%total != 0: 
                    continue 

                cur_num = (j*n)//total
                if cur_num != 0 and cur_num != n and dp[j] & (1 << cur_num):
                    return True 

        return False 


if __name__ == "__main__": 
    s = Solution() 

    nums = [3,1]
    assert not s.splitArraySameAverage(nums)

