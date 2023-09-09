from typing import * 
import math 
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        
        def validTime(t): 
            nonlocal ranks 
            nonlocal cars
            res = 0 
            for r in ranks:
                res += int(math.sqrt(t/r))
                if res >= cars: 
                    return True 
            return False 
        
        maxt = ranks[-1]*(cars**2)
        l, r = 1, maxt 
        while l <= r: 
            mid = (r-l)//2 + l 
            if validTime(mid): 
                r = mid - 1 
            else: 
                l = mid + 1 
                
        return r+1  
         