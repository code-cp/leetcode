#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

from typing import * 

# @lc code=start
class Solution:
    def checkDivide(self, num):
        n = num 
        while n > 0: 
            t = n % 10 
            if t == 0: 
                return False 
            n //= 10  
            if num % t != 0: 
                return False
        return True 
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if self.checkDivide(i):
                res.append(i)
        return res 

# @lc code=end

if __name__ == "__main__": 
    s = Solution()

    left = 1 
    right = 22 
    result = s.selfDividingNumbers(left, right)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22] 
