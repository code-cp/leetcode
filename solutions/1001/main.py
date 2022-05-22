from collections import defaultdict
from typing import List 

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # initialize containers 
        lamp_set = set()
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        diag_count = defaultdict(int)
        bdiag_count = defaultdict(int)
        
        # add lamps 
        for l in lamps: 
            lamp_set.add((l[0], l[1]))
        for l in lamp_set:
            row_count[l[0]] += 1 
            col_count[l[1]] += 1 
            diag_count[l[0]-l[1]] += 1
            bdiag_count[l[0]+l[1]] += 1 
            
        # traverse queries 
        ans = [0] * len(queries)
        dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,0], [0,1], [1,-1], [1,0], [1,1]]
        for i, q in enumerate(queries):
            if row_count[q[0]] > 0 or col_count[q[1]] > 0 or diag_count[q[0]-q[1]] > 0 or bdiag_count[q[0]+q[1]] > 0: 
                ans[i] = 1
            for d in dirs: 
                x, y = q[0]+d[0], q[1]+d[1]
                if x < 0 or x > n-1 or y < 0 or y > n-1: 
                    continue 
                if (x, y) in lamp_set: 
                    lamp_set.remove((x, y))
                    row_count[x] -= 1 
                    col_count[y] -= 1 
                    diag_count[x-y] -= 1 
                    bdiag_count[x+y] -= 1 
        return ans 

if __name__ == "__main__": 
    s = Solution()
    n = 5
    lamps = [[0,0],[4,4]]
    queries = [[1,1],[1,0]]
    assert s.gridIllumination(n, lamps, queries) == [1,0]