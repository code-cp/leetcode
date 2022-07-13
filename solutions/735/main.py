from typing import * 

from collections import deque 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for a in asteroids:
            if a > 0 or len(stack) == 0:
                stack.append(a)
                continue 
            while len(stack) > 0: 
                temp = stack[-1]
                if temp < 0:
                    stack.append(a)
                    break 
                if temp > abs(a):
                    break 
                elif temp == abs(a):
                    stack.pop()
                    break 
                else: 
                    stack.pop()
                    if len(stack) == 0:
                        stack.append(a)
                        break 
        res = []
        while len(stack) > 0: 
            res.append(stack[-1])
            stack.pop()
        res.reverse()
        return res
            

if __name__ == "__main__":
    s = Solution()

    # asteroids = [5,10,-5]
    # assert s.asteroidCollision(asteroids) == [5,10]

    # asteroids = [8,-8]
    # assert s.asteroidCollision(asteroids) == []

    asteroids = [-2,-1,1,2]
    assert s.asteroidCollision(asteroids) == [-2,-1,1,2]