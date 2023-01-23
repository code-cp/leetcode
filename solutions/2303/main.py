from typing import * 

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0 
        pre = 0 
        for b in brackets: 
            if income >= b[0]: 
                diff = b[0] - pre 
                res += diff*b[1]/100
                pre = b[0]
            else: 
                res += (income-pre)*b[1]/100
                break 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    brackets = [[3,50],[7,10],[12,25]]
    income = 10
    assert s.calculateTax(brackets, income) == 2.65