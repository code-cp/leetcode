from typing import * 

from collections import deque 
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = deque()
        res = []
        j = 0 
        for i in range(1, n+1): 
            stack.append(i)
            res.append("Push")
            if i == target[j]: 
                j += 1
            else: 
                if len(stack) > 0:
                    stack.pop()
                    res.append("Pop") 
            if j == len(target): 
                return res 

if __name__ == "__main__": 
    s = Solution() 

    target = [1,2]
    n = 4
    assert s.buildArray(target, n)

    target = [1,3]
    n = 3
    assert s.buildArray(target, n)