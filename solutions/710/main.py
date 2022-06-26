from typing import * 

import random 
from collections import deque, defaultdict  
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.hashmap = defaultdict(int)
        s = len(blacklist)
        bl = deque()
        # [0, N-s)内的元素，如果有i个在黑名单中，那么在[N-s, N)中，必定有i个元素不在黑名单中
        self.m = n - s 
        for b in self.blacklist: 
            # 注意边界条件
            if b >= self.m: 
                break 
            bl.append(b)
        for i in range(self.m, n):
            if i in self.blacklist: 
                continue 
            b = bl.popleft()
            self.hashmap[b] = i 

    def pick(self) -> int:
        # 注意边界条件
        i = random.randint(0, self.m-1)
        if i in self.blacklist: 
            return self.hashmap[i]
        else: 
            return i

if __name__ == "__main__": 
    n = 3
    blacklist = [2, 0]
    s = Solution(n, blacklist)
    print(s.pick())
    print(s.pick())
    print(s.pick())
    print(s.pick())
    print(s.pick())