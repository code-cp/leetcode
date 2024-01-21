from typing import * 

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cheapest = [float("inf")]*2 
        for p in prices: 
            if p < cheapest[0]:
                cheapest[1] = cheapest[0]
                cheapest[0] = p 
            elif p < cheapest[1]:
                cheapest[1] = p  
                
        diff = money - sum(cheapest)
        if diff < 0: 
            return money
        else: 
            return diff  