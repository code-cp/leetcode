from typing import * 

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = -1
        cur = [0, 0]
        for c in coins: 
            if cur[0]+c <= cur[1]+1 and cur[1]+c >= cur[1]+1: 
                cur[1] += c 
            else: 
                res = max(res, cur[1]-cur[0]+1)
                cur = [c, c]
        res = max(res, cur[1]-cur[0]+1)
        return res 

if __name__ == "__main__": 
    s = Solution() 

    coins = [1,1,1,4]
    assert s.getMaximumConsecutive(coins) == 8

    coins = [1,3]
    assert s.getMaximumConsecutive(coins) == 2 