from collections import deque 
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n 
        stack = deque()
        for l in logs:
            info = l.split(":")
            if info[1] == "start": 
                stack.append(int(info[2]))
                accu = 0 
            else: 
                start = stack.pop()
                idx = int(info[0])
                diff = int(info[2]) - start 
                res[idx] += diff+1
                accu += diff+1

                if len(stack) > 0:
                    start = stack.pop()
                    start += accu
                    stack.append(start)
        return res 