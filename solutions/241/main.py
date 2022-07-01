from typing import * 
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def operator(a, o, b): 
            if o == '+':
                return a + b 
            if o == '-': 
                return a - b 
            if o == '*': 
                return a * b 

        # preprocess expression
        n = len(expression)
        i = 0 
        cur = ""
        expr = []
        while i < n: 
            j = i 
            while j < n: 
                if expression[j].isdigit():
                    cur += expression[j]
                else: 
                    break 
                j += 1 
            expr.append(int(cur))
            cur = ""
            if j < n: 
                expr.append(expression[j])
            i = j+1 

        @lru_cache
        def dfs(l: int, r: int) -> List[int]:
            if l == r:
                return [expr[l]]
            res = []
            for i in range(l, r, 2):
                left = dfs(l, i)
                right = dfs(i + 2, r)
                for x in left:
                    for y in right:
                        res.append(operator(x, expr[i+1], y))
            return res
        return dfs(0, len(expr)-1)

if __name__ == "__main__":
    s = Solution()

    # expression = "2-1-1"
    # print(s.diffWaysToCompute(expression)) 

    expression = "2*3-4*5"
    print(s.diffWaysToCompute(expression)) 