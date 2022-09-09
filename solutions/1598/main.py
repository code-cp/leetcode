from typing import * 

from collections import deque 
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        for l in logs: 
            if l == "../":
                if len(stack) == 0: 
                    pass 
                else: 
                    stack.pop()
            elif l == "./": 
                pass 
            else: 
                stack.append(l.split("/")[0])
        return len(stack)

if __name__ == "__main__": 
    s = Solution()

    logs = ["d1/","d2/","../","d21/","./"]
    assert s.minOperations(logs) == 2 

    logs = ["d1/","d2/","./","d3/","../","d31/"]
    assert s.minOperations(logs) == 3

    logs = ["d1/","../","../","../"]
    assert s.minOperations(logs) == 0