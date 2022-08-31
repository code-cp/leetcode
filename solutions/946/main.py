from typing import * 

from collections import deque 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        j = 0 
        for i, p in enumerate(pushed): 
            while j < len(popped) and len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1 
            if j < len(popped) and p == popped[j]:
                j += 1 
            else: 
                stack.append(p)
        while len(stack) > 0: 
            val = stack.pop()
            if j >= len(popped) or val != popped[j]:
                return False 
            else: 
                j += 1 
        return True 

if __name__ == "__main__": 
    s = Solution()

    # pushed = [1,2,3,4,5]
    # popped = [4,5,3,2,1]
    # assert s.validateStackSequences(pushed, popped)

    # pushed = [1,2,3,4,5]
    # popped = [4,3,5,1,2]
    # assert not s.validateStackSequences(pushed, popped)

    # pushed = [2,1,0]
    # popped = [1,2,0]
    # assert s.validateStackSequences(pushed, popped)

    pushed = [1,2,3,0]
    popped = [2,1,3,0]
    assert s.validateStackSequences(pushed, popped)
