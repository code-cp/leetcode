from typing import * 

from collections import defaultdict 
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def dfs(state, curr, target, memo):
            for i in range(1, maxChoosableInteger+1):
                if (state >> i) & 1 == 0: 
                    if memo[state] != 0: 
                        return True if memo[state] == 1 else False 
                    if curr + i >= target or not dfs(state | (1 << i), curr + i, target, memo):
                        memo[state] = 1 
                        return True
            memo[state] = 2 
            return False 

        if (1+maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal: 
            return False 

        memo = defaultdict(int)
        return dfs(0, 0, desiredTotal, memo) 

if __name__ == "__main__": 
    s = Solution()
    
    assert not s.canIWin(10, 11)
    assert not s.canIWin(5, 50)