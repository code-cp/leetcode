from typing import * 
from collections import defaultdict 

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center_candidate = defaultdict(int)
        for e in edges: 
            center_candidate[e[0]] += 1
            center_candidate[e[1]] += 1
            if center_candidate[e[0]] > 1: 
                return e[0]
            if center_candidate[e[1]] > 1: 
                return e[1]

if __name__ == "__main__": 
    edges = [[1,2],[2,3],[4,2]]
    s = Solution()
    assert s.findCenter(edges) == 2 