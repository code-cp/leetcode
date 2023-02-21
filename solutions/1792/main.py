from typing import * 

class Entry: 
    __slots__ = "p", "t"

    def __init__(self, p: int, t: int): 
        self.p = p 
        self.t = t 

    def __lt__(self, b: "Entry") -> bool: 
        # used to define or implement the functionality of the less than operator “<”
        m = (self.p+1)/(self.t+1)
        n = self.p/self.t 
        c = (b.p+1)/(b.t+1)
        d = b.p/b.t 
        # python has min heap 
        return m-n > c-d 

import heapq 
import math 
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapq.heapify(h)
        for _ in range(extraStudents): 
            # Pop and return the smallest item from the heap, and also push the new item
            heapq.heapreplace(h, Entry(h[0].p+1, h[0].t+1))
        res = sum(e.p/e.t for e in h)/len(h)
        return res 

if __name__ == "__main__": 
    s = Solution() 

    classes = [[1,2],[3,5],[2,2]]
    extraStudents = 2
    assert math.isclose(s.maxAverageRatio(classes, extraStudents), 0.78333, abs_tol=0.01)