from typing import * 

from collections import deque 
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def validMut(s: str, t: str) -> bool:
            res = 0
            for a, b in zip(s, t): 
                if a != b: 
                    res += 1 
            return res == 1 
        queue = deque()
        queue.append((start, 0)) 
        visited = set() 
        visited.add(start)
        while queue: 
            curr, dist = queue.popleft() 
            if curr == end: 
                return dist 
            visited.add(curr) 
            for b in bank: 
                if validMut(curr, b) and b not in visited: 
                    queue.append((b, dist + 1)) 
                    visited.add(b) 
        return -1  

if __name__ == "__main__":
    s = Solution() 

    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    assert s.minMutation(start, end, bank) == 1 

    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    assert s.minMutation(start, end, bank) == 2 