from typing import * 

import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calTime(piles, h, k): 
            return sum(math.ceil(p / k) for p in piles) 
        l, r = 1, max(piles) 
        while l <= r:
            mid = (r - l) // 2 + l 
            if calTime(piles, h, mid) <= h:
                # 如果r = mid - 1后导致r<l，说明l等于mid
                r = mid - 1 
            elif calTime(piles, h, mid) > h:
                # 注意返回l不是l-1
                l = mid + 1 
        return l  

if __name__ == "__main__": 
    s = Solution() 

    # piles = [3,6,7,11]
    # h = 8
    # assert s.minEatingSpeed(piles, h) == 4

    piles = [30,11,23,4,20]
    h = 6
    assert s.minEatingSpeed(piles, h) == 23 
