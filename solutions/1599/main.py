from typing import * 

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        calcProf = lambda onboard, i: boardingCost * onboard - runningCost * i

        wait = onboard = max_profit = max_i = 0 
        max_cap = 4 
        for i, c in enumerate(customers):
            wait += c
            # update people number 
            onboard += min(max_cap, wait)
            wait -= min(max_cap, wait)
            # update profit 
            i += 1 
            profit = calcProf(onboard, i)
            if profit > max_profit: 
                max_profit = profit 
                max_i = i
        while wait > 0: 
            onboard += min(max_cap, wait)
            wait -= min(max_cap, wait) 
            i += 1 
            profit = calcProf(onboard, i)
            if profit > max_profit: 
                max_profit = profit 
                max_i = i
        return max_i if max_profit > 0 else -1 
        

if __name__ == "__main__": 
    s = Solution() 

    customers = [8,3]
    boardingCost = 5
    runningCost = 6
    assert s.minOperationsMaxProfit(customers, boardingCost, runningCost) == 3 