from typing import * 

# tle 
# [5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5114,5115,5116,5117,5118,5119,5120,5121,5122,5123,5124,5125,5126,5127,6128,7724]

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # avg1*x + avg2*y = avg*(x+y)
        # avg1 = avg2 
        # avg1*(x+y) = avg*(x+y)
        # avg*(x+y) - avg*x = avg*y 
        
        # total / (x+y) = total1 / x 
        # total * x = total1 * (x+y)
        # 1<=x<=30

        n = len(nums)
        if n == 1: 
            return False

        nums.sort(reverse=True)
        total = sum(nums)

        def dfs(cur_sum, cur_num, cur_idx, total_num):
            # base case
            # NOTE, this should be checked first 
            if cur_num == total_num and cur_num != n:
                if cur_sum * n == cur_num * total: 
                    return True  
            if cur_num > total_num: 
                return False 
            if cur_idx >= n: 
                return False 

            if dfs(cur_sum+nums[cur_idx], cur_num+1, cur_idx+1, total_num):
                return True 

            # skip the duplicates 
            j = cur_idx+1
            while j < n and nums[j] == nums[cur_idx]:
                j += 1 

            return dfs(cur_sum, cur_num, j, total_num)

        # NOTE, end is n//2+2, not n//2+1 
        for i in range(1, n//2+2):
            if (total * i) % n != 0:
                continue 
            if dfs(0, 0, 0, i):
                return True 

        return False 


if __name__ == "__main__": 
    s = Solution() 

    nums = [3,1]
    assert not s.splitArraySameAverage(nums)

