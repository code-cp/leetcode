from typing import * 

from collections import deque 
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = deque()
        primitives = [[]] 
        count = 0 
        for p in s: 
            primitives[count].append(p) 
            if p == "(":
                stack.append(p) 
            else: 
                stack.pop() 
                if len(stack) == 0: 
                    primitives.append([]) 
                    count += 1 
        res = ""
        for p in primitives: 
            res += "".join(p[1:-1])
        return res  

if __name__ == "__main__": 
    sol = Solution()

    s = "(()())(())"
    assert sol.removeOuterParentheses(s) == "()()()" 