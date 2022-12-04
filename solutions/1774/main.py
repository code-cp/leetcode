from typing import * 

class Solution:
    def backtrack(self, target, toppingCosts, cur, start_idx):
        if cur == target: 
            self.res = target
            return 
        if abs(target-cur) < abs(target-self.res): 
            self.res = cur  
        elif abs(target-cur) == abs(target-self.res):
            if cur < self.res: 
                self.res = cur 
        else:
            if cur > self.res: 
                return 

        for t in range(start_idx, len(toppingCosts)):
            for i in range(3):
                # NOTE, t+1 not start_idx+1
                self.backtrack(target, toppingCosts, cur+i*toppingCosts[t], t+1)

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        baseCosts.sort()
        toppingCosts.sort()
        self.res = float("inf")
        for cur in baseCosts: 
            self.backtrack(target, toppingCosts, cur, 0)
            if self.res == target: 
                return target 
        return self.res 


if __name__ == "__main__": 
    s = Solution() 

    # baseCosts = [10]
    # toppingCosts = [1]
    # target = 1
    # assert s.closestCost(baseCosts, toppingCosts, target) == 10

    baseCosts = [1,7]
    toppingCosts = [3,4]
    target = 10
    assert s.closestCost(baseCosts, toppingCosts, target) == 10 