from typing import List 

class Solution:
    def dfs(self, grid, visited, i, j): 
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        que = []
        cells = set()

        que.append((i, j))
        while len(que) > 0: 
            # use dfs instead of bfs to avoid TLE 
            i, j = que.pop()
            visited[i][j] = 1 
            cells.add((i, j))
            for d in dirs: 
                x, y = i+d[0], j+d[1]
                if x < 0 or x > self.m-1 or y < 0 or y > self.n-1:
                    # (self.m, self.n) is dummy node for boundary 
                    cells.add((self.m, self.n))
                    continue  
                if grid[x][y] == 0: 
                    continue 
                if visited[x][y] == 1: 
                    continue 
                que.append((x, y))

        return cells 
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # initialize graph 
        self.m, self.n = len(grid), len(grid[0])
        graph = [[] for _ in range(self.m*self.n)]
        visited = [[0] * self.n for _ in range(self.m)]
        # add edges 
        for i in range(self.m): 
            for j in range(self.n): 
                if grid[i][j] == 0: 
                    continue  
                if visited[i][j] == 1: 
                    continue    
                # NOTE, not i*j
                idx = i*self.n+j 
                neighbors = self.dfs(grid, visited, i, j)
                graph[idx] += list(neighbors)
        # traverse the graph 
        result = 0   
        for i in range(self.m):
            for j in range(self.n): 
                # NOTE, not i*j
                idx = i*self.n+j 
                if len(graph[idx]) == 0: 
                    continue 
                if (self.m, self.n) in graph[idx]: 
                    continue     
                result += len(graph[idx])

        return result  

if __name__ == "__main__": 
    s = Solution()
    grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
    assert s.numEnclaves(grid) == 3 