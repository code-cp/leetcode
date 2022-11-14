from typing import * 

# tle 
# [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]

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

        total = sum(nums)
        target = total / n 

        def dfs(cur_sum, cur_num, cur_idx, total_num):
            # base case
            if cur_num > total_num: 
                return False 
            if cur_num == n: 
                return False 
            if cur_idx >= n: 
                return False 
            if cur_num != 0:
                if cur_sum / cur_num == target and cur_num == total_num: 
                    return True  
                if cur_sum / cur_num > target: 
                    return False 

            return (dfs(cur_sum+nums[cur_idx], cur_num+1, cur_idx+1, total_num) or
                dfs(cur_sum, cur_num, cur_idx+1, total_num)) 

        for i in range(1, n):
            if (total * i) % n != 0:
                continue 
            if dfs(0, 0, 0, i):
                return True 

        return False 


if __name__ == "__main__": 
    s = Solution() 

    nums = [72,56,81,54,15,96,80,90,8]
    assert s.splitArraySameAverage(nums)