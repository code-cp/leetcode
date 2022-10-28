from typing import * 

from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        M = 1e9 + 7 

        left_min = [0] * n 
        stack = deque() 
        stack.append((arr[0], 0))
        for i in range(1, n): 
            # NOTE, use >= 
            # stack is from large to small numbers 
            while len(stack) > 0 and arr[i] <= stack[-1][0]:
                _, j = stack.pop()
                left_min[i] += j+1  
            stack.append((arr[i], left_min[i]))

        right_min = [0] * n 
        stack = deque()
        stack.append((arr[-1], 0))
        for i in range(n-2, -1, -1):
            while len(stack) > 0 and arr[i] < stack[-1][0]:
                _, j = stack.pop()
                right_min[i] += j+1  
            stack.append((arr[i], right_min[i]))

        res = 0 
        for i in range(n): 
            res += arr[i] * (((left_min[i]+1) * (right_min[i]+1)) % M) % M 
            res %= M 

        return int(res) 

if __name__ == "__main__": 
    s = Solution() 

    arr = [71,55,82,55]
    assert s.sumSubarrayMins(arr) == 593 

    arr = [3,1,2,4]
    assert s.sumSubarrayMins(arr) == 17 