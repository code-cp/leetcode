from typing import * 
from collections import deque 
import heapq 

# A* algorithm 
# Imagine you are in a maze and you want to find the shortest path from your current location to a goal destination. The A* algorithm helps you make the right decisions to reach your goal efficiently.

# Here's how it works:

# You start at your current location and create a list of all the neighboring locations you can move to from there.

# For each neighboring location, you calculate two values: the cost to reach that location from your starting point (called the "g-value"), and an estimate of the remaining distance from that location to the goal (called the "h-value").

# The A* algorithm uses a priority queue, which is a data structure that allows you to prioritize elements based on their values. In this case, the priority is determined by a combination of the g-value and the h-value. The lower the sum of these values, the higher the priority.

# You add your current location to the priority queue and start exploring the neighboring locations with the highest priority.

# For each neighboring location, you calculate its g-value and h-value, and update them if necessary. Then you add the location to the priority queue.

# You continue this process, always exploring the location with the highest priority from the queue. This ensures that you prioritize locations that are closer to the goal.

# As you explore locations, you keep track of the path you have taken so far.

# When you reach the goal destination, you have found the shortest path!

# The A* algorithm is considered efficient because it combines the information about the cost to reach a location (g-value) and the estimated distance remaining to the goal (h-value) to make intelligent decisions about which locations to explore first. By considering both factors, it tends to find the shortest path more quickly than other algorithms.

# g : history = # of pushes
# h: heuristics = Manhattan distance from the current box position to the target position, always <= actual moves.
# f = g + h

class Node: 
    def __init__(self, bx=0, by=0, px=0, py=0, h=0, g=0): 
        self.bx = bx 
        self.by = by 
        self.px = px 
        self.py = py 
        self.h = h 
        self.g = g    

    def get_cost(self): 
        return self.h + self.g 

    def __lt__(self, other): 
        return self.get_cost() < other.get_cost()
    
    def __gt__(self, other): 
        return self.get_cost() > oher.get_cost()

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

            visited = [[0]*m for _ in range(n)]
            q = deque()
            q.append((cur.px, cur.py))
            visited[cur.py][cur.px] = 1 
            while len(q) > 0: 
                x, y = q.popleft()
                for d in dirs: 
                    nx, ny = x+d[0], y +d[1]
                    if visited[ny][nx] == 1: 
                        continue 
                    visited[ny][nx] = 1
                    if not isValid(nx, ny): 
                        continue 
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
            
            next_node.g = cur.g + 1 
            next_node.h = abs(next_node.bx - end.bx) + abs(next_node.by - end.by)
            
            if not isValid(next_node.bx, next_node.by): 
                return False, next_node 

            tx = cur.bx - dx
            ty = cur.by - dy 
            return hasPath(cur, tx, ty), next_node
            
        hq = []
        start.g = 0 
        start.h = abs(start.bx-end.bx) + abs(start.by-end.by)
        heapq.heappush(hq, (start.get_cost(), start))
        visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
        
        while len(hq) > 0: 
            cost, cur = heapq.heappop(hq)
            for d in dirs: 
                can_push, next_node = canPush(cur, d[0], d[1])
                if visited[next_node.by][next_node.bx][next_node.py][next_node.px]:
                    continue 
                visited[next_node.by][next_node.bx][next_node.py][next_node.px] = 1 
                if not can_push: 
                    continue 
                if next_node.bx == end.bx and next_node.by == end.by: 
                    return next_node.g 
                heapq.heappush(hq, (next_node.get_cost(), next_node))
                
        return -1 
    
if __name__ == "__main__": 
    s = Solution()
    
    grid = [["#","#","#","#","#","#"],
                ["#","T","#","#","#","#"],
                ["#",".",".","B",".","#"],
                ["#",".","#","#",".","#"],
                ["#",".",".",".","S","#"],
                ["#","#","#","#","#","#"]]
    assert s.minPushBox(grid) == 3 