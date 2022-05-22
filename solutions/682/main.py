from typing import * 
from collections import deque 

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = deque()
        special = ["+", "D", "C"]
        for op in ops: 
            if op not in special: 
                stack.append(int(op))
            else: 
                if op == "+":
                    pre1 = stack.pop()
                    pre2 = stack[-1] 
                    stack.append(pre1)
                    score = pre1 + pre2 
                    stack.append(score)
                elif op == "D": 
                    score = stack[-1]*2 
                    stack.append(score)
                elif op == "C": 
                    stack.pop()
        return sum(stack) 

if __name__ == "__main__": 
    s = Solution()
    
    ops = ["5","2","C","D","+"]
    assert s.calPoints(ops) == 30 