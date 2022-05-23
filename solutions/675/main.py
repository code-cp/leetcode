# 675. Cut Off Trees for Golf Event
from typing import * 

from collections import deque 
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def bfs(m, n, start, end): 
            q = deque([(start, 0)])
            visited = set()
            while q: 
                cur, steps = q.popleft()
                if cur == end: 
                    return steps
                if cur in visited: 
                    continue
                visited.add(cur)
                for d in dirs: 
                    x, y = cur[0] + d[0], cur[1] + d[1]
                    if 0 <= x < m and 0 <= y < n and forest[x][y] > 0:
                        q.append(((x, y), steps + 1))
            return -1 

        trees = []
        m, n = len(forest), len(forest[0]) 
        for i in range(m): 
            for j in range(n): 
                if forest[i][j] > 1: 
                    trees.append([forest[i][j], i, j])
        trees = sorted(trees, key=lambda x: x[0])
        min_steps = 0 
        cur = [0, 0]
        for t in trees: 
            step = bfs(m, n, (cur[0], cur[1]), (t[1], t[2]))
            cur = t[1:]
            if step == -1: 
                return -1 
            min_steps += step 
        return min_steps

if __name__ == "__main__": 
    s = Solution() 

    forest = [[1,2,3],[0,0,4],[7,6,5]]
    assert s.cutOffTree(forest) == 6 