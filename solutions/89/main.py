from typing import List 

class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [0] * (1 << n)
        for i in range(1, n+1):
            count = 1 << i
            toAdd = 1 << (i-1)
            for j in range(count//2, count):
                dp[j] = dp[count-1-j]+toAdd
        return dp

if __name__ == "__main__": 
    n = 2 
    s = Solution()
    assert s.grayCode(n) == [0,1,3,2]
