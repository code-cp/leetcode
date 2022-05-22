from typing import * 

from collections import deque 
class RecentCounter:

    def __init__(self):
        self.stack = deque()
        self.num = 0 

    def ping(self, t: int) -> int:
        while self.num > 0 and self.stack[0] < t - 3000:
            self.stack.popleft()  
            self.num -= 1 
        self.stack.append(t)
        self.num += 1 
        return self.num

if __name__ == "__main__": 
    obj = RecentCounter()
    t = 1 
    assert obj.ping(t) == 1 
    t = 100
    assert obj.ping(t) == 2 
    t = 3001 
    assert obj.ping(t) == 3 
    t = 3002 
    assert obj.ping(t) == 3 