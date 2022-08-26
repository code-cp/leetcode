from typing import * 

import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        stack = nums[:2]
        heapq.heapify(stack)
        for num in nums[2:]:
            if num > stack[0]:
                heapq.heappop(stack)
                heapq.heappush(stack, num)
        a = heapq.heappop(stack)
        b = heapq.heappop(stack)
        return (a-1)*(b-1)