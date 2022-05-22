from typing import *

class State: 
    def __init__(self): 
        self.value = 0 
        self.str = ""

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # dp table 
        n = len(nums)
        dp = [[[State() for _ in range(2)] for _ in range(n)] for _ in range(n)] 

        # initialize 
        for i in range(n): 
            for j in range(2): 
                dp[i][i][j].value = nums[i]
                dp[i][i][j].str = str(nums[i])
        for i in range(n): 
            for j in range(i+1, n): 
                dp[i][j][0].value = 1e5 
                dp[i][j][1].value = 1e-5

        # traverse 
        for i in range(n):
            for j in range(n - i):
                for k in range(j, j + i):
                    maxVal = dp[j][k][1].value / dp[k+1][j+i][0].value
                    if dp[j][j+i][1].value < maxVal: 
                        dp[j][j+i][1].value = maxVal
                        if k == j+i-1:
                            dp[j][j+i][1].str = dp[j][k][1].str + "/" + dp[k+1][j+i][0].str
                        else: 
                            dp[j][j+i][1].str = dp[j][k][1].str + "/(" + dp[k+1][j+i][0].str + ")"
                    
                    minVal = dp[j][k][0].value / dp[k+1][j+i][1].value
                    if dp[j][j+i][0].value > minVal:
                        dp[j][j+i][0].value = minVal
                        if k == j+i-1:
                            dp[j][j+i][0].str = dp[j][k][0].str + "/" + dp[k+1][j+i][1].str
                        else: 
                            dp[j][j+i][0].str = dp[j][k][0].str + "/(" + dp[k+1][j+i][1].str + ")"

        # return result 
        result = dp[0][n-1][1].str 
        return result

if __name__ == "__main__":
    s = Solution() 
    nums = [1000,100,10,2]
    assert s.optimalDivision(nums) == "1000/(100/10/2)"
    nums = [1000,2]
    assert s.optimalDivision(nums) == "1000/2"