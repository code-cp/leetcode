#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#

# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        # due to symmetry 
        target = abs(target)
        x = count = 0 

        def dfs(x, target, count): 
            # base case 
            if x > target: 
                return float("inf") 
            if x == target: 
                return count 

            count1 = dfs(x+1, target, count+2)
            count2 = dfs(x+count+1, target, count+1)

            return min(count1, count2)

        count = dfs(x, target, count)
        return count 
