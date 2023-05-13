from typing import * 
from collections import deque 
import heapq

class Node: 
    def __init__(self, bx=0, by=0, px=0, py=0, h=0, g=0): 
        self.bx = bx 
        self.by = by 
        self.px = px 
        self.py = py 

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(grid)
        m = len(grid[0])
        
        start = Node()
        end = Node()
        
        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == "B": 
                    start.by = i 
                    start.bx = j 
                elif grid[i][j] == "S": 
                    start.px = j  
                    start.py = i 
                elif grid[i][j] == "T": 
                    end.by = i 
                    end.bx = j 
                    
        def isValid(x, y): 
            if x < 0 or x >= m or y < 0 or y >= n: 
                return False  
            if grid[y][x] == "#": 
                return False 
            return True 
        
        def hasPath(cur, tx, ty): 
            if not isValid(tx, ty): 
                return False 
            # NOTE, do not forget this 
            if cur.px == tx and cur.py == ty: 
                return True 
    
            visited = [[0]*m for _ in range(n)]
            q = deque()
            q.append((cur.px, cur.py))
            visited[cur.py][cur.px] = 1 
            while len(q) > 0: 
                x, y = q.popleft()
                for d in dirs: 
                    nx, ny = x+d[0], y +d[1]
                    if not isValid(nx, ny): 
                        continue 
                    # NOTE, check valid first, then check visited 
                    if visited[ny][nx] == 1: 
                        continue 
                    visited[ny][nx] = 1
                    if nx == cur.bx and ny == cur.by: 
                        continue 
                    if nx == tx and ny == ty: 
                        return True 
                    q.append((nx, ny))
            
            return False 
        
        def canPush(cur, dx, dy):
            next_node = Node() 
            next_node.bx = cur.bx + dx
            next_node.by = cur.by + dy 
            next_node.px = cur.bx 
            next_node.py = cur.by 
            
            if not isValid(next_node.bx, next_node.by): 
                return False, next_node 

            # check whether the person can teleport to this position near the box
            tx = cur.bx - dx
            ty = cur.by - dy 
            
            return hasPath(cur, tx, ty), next_node
            
        q = deque()
        q.append(start)
        visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
        visited[start.by][start.bx][start.py][start.px] = 1
        ans = 1 
        
        while len(q) > 0: 
            q_len = len(q)
            for _ in range(q_len): 
                cur = q.popleft()
                for d in dirs: 
                    can_push, next_node = canPush(cur, d[0], d[1])
                    if not can_push: 
                        continue 
                    if visited[next_node.by][next_node.bx][next_node.py][next_node.px]:
                        continue 
                    visited[next_node.by][next_node.bx][next_node.py][next_node.px] = 1 
                    if next_node.bx == end.bx and next_node.by == end.by: 
                        return ans 
                    q.append(next_node)
            ans += 1 
                
        return -1 
    
if __name__ == "__main__": 
    s = Solution()
    
    # grid = [["#","#","#","#","#","#"],
    #             ["#","T","#","#","#","#"],
    #             ["#",".",".","B",".","#"],
    #             ["#",".","#","#",".","#"],
    #             ["#",".",".",".","S","#"],
    #             ["#","#","#","#","#","#"]]
    # assert s.minPushBox(grid) == 3 

    grid = [["#",".",".","#","#","#","#","#"],["#",".",".","T","#",".",".","#"],["#",".",".",".","#","B",".","#"],["#",".",".",".",".",".",".","#"],["#",".",".",".","#",".","S","#"],["#",".",".","#","#","#","#","#"]]
    s.minPushBox(grid) 