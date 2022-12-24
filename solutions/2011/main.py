from typing import * 

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0 
        for opt in operations: 
            if opt[0] == "+" or opt[-1] == "+": 
                res += 1 
            else: 
                res -= 1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    operations = ["--X","X++","X++"]
    assert s.finalValueAfterOperations(operations) == 1 