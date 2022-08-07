from typing import * 

from collections import deque 
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n 
        stack = deque()
        for l in logs:
            info = l.split(":")
            if info[1] == "start": 
                stack.append([int(info[0]), int(info[2])])
            else: 
                idx, start = stack.pop()
                diff = int(info[2]) - start + 1
                res[idx] += diff

                if len(stack) > 0:
                    idx, start = stack[-1]
                    res[idx] -= diff
        return res 

if __name__ == "__main__":
    s = Solution()

    # n = 2
    # logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    # assert s.exclusiveTime(n, logs) == [3,4]

    # n = 1
    # logs = ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]
    # assert s.exclusiveTime(n, logs) == [6]

    n = 8
    logs = ["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]
    assert s.exclusiveTime(n, logs) == [20,14,35,7,6,9,10,14]
