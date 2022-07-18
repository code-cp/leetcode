from typing import * 

class Solution:
    def dfs(self, grid, r, c, next_infect, visited, curr):
        m, n = len(grid), len(grid[0])
        walls = 0 
        # base case
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 2:
            return walls 
        if grid[r][c] == 0: 
            walls += 1 
            next_infect.add((r, c))
            return walls 
        else:
            if visited[r][c] == 1:
                return walls

        visited[r][c] = 1 
        curr.append((r, c))
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        for d in dirs: 
            walls += self.dfs(grid, r+d[0], c+d[1], next_infect, visited, curr)
        return walls

    def containVirus(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0 
        while True: 
            visited = [[0]*n for _ in range(m)]
            virus_area = []
            all_nexts = []
            max_idx, max_walls = -1, -1 
            for r in range(m):
                for c in range(n): 
                    if grid[r][c] != 1 or visited[r][c] == 1: 
                        continue 
                    curr = []
                    next_infect = set()
                    walls = self.dfs(grid, r, c, next_infect, visited, curr)
                    if len(next_infect) == 0: 
                        continue 
                    if len(all_nexts) == 0 or len(next_infect) > len(all_nexts[max_idx]):
                        virus_area = curr 
                        max_idx = len(all_nexts) 
                        max_walls = walls 
                    all_nexts.append(next_infect) 
            # check if no more cells can be infected 
            if len(all_nexts) == 0: 
                break 
            total += max_walls 
            for i in range(len(all_nexts)):
                if i == max_idx: 
                    for key in virus_area: 
                        r, c = key[0], key[1]
                        grid[r][c] = 2 
                else: 
                    for key in all_nexts[i]: 
                        r, c = key[0], key[1]
                        grid[r][c] = 1 
        return total 

if __name__ == "__main__": 
    s = Solution()

    isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
    assert s.containVirus(isInfected) == 10 