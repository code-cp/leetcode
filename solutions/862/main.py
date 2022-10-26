from typing import * 

from collections import deque 
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1): 
            presum[i] = presum[i-1] + nums[i-1]
        
        res = float("inf")
        stack = deque()
        for i in range(n+1):
            # remove the values at back of stack 
            while len(stack) > 0 and presum[stack[-1]] >= presum[i]:
                stack.pop()
            # remove the values at the front of stack 
            while len(stack) > 0 and presum[i] - presum[stack[0]] >= k: 
                # since we use i-stack[0], need to use for i in range(n+1) instead of for i in range(1, n+1)
                res = min(res, i-stack[0])
                stack.popleft()
            stack.append(i)

        return res if res != float("inf") else -1 

if __name__ == "__main__": 
    s = Solution() 

    nums = [77,19,35,10,-14]
    k = 19
    assert s.shortestSubarray(nums, k) == 1

    nums = [2,-1,2]
    k = 3
    assert s.shortestSubarray(nums, k) == 3