from typing import * 

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        while sum(amount) != 0:
            amount.sort()
            amount[2] -= 1 
            if amount[1] > 0:
                amount[1] -= 1 
            res += 1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    amount = [5,4,4]
    assert s.fillCups(amount) == 7

    # amount = [1,4,2]
    # assert s.fillCups(amount) == 4
