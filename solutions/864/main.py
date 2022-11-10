from typing import * 

from collections import deque 
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        grid_new = [[0 for _ in range(n)] for _ in range(m)]

        all_keys = []
        for i in range(m): 
            for j in range(n):
                if grid[i][j].isalpha():
                    if grid[i][j].islower(): 
                        all_keys.append(grid[i][j])
                elif grid[i][j] == "@": 
                    start = (i, j, 0, 0)
                grid_new[i][j] = grid[i][j]

        # NOTE how to create visited 
        # lst = [[ ['#' for values in range(a)] for col in range(b)] for row in range(c)]
        visited = [[[0 for _ in range(2**len(all_keys))] for _ in range(n)] for _ in range(m)]
        grid = grid_new 
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        # NOTE, cannot use list 
        keys = 0
        que = deque()
        que.append(start)
        visited[start[0]][start[1]][keys] = 1 

        # BFS 
        # 1. global step  
        # 2. keep move in state 
        while que: 
            q_len = len(que)
            for _ in range(q_len): 
                cell = que.popleft()
                r, c, move, keys = cell
                if grid[r][c].islower(): 
                    idx = all_keys.index(grid[r][c])
                    if keys & (1 << idx) == 0:
                        keys |= 1 << idx 
                    if keys == 2 ** len(all_keys) - 1: 
                        return move  
                for d in dirs: 
                    new_r, new_c = r+d[0], c+d[1]
                    if new_r > m-1 or new_r < 0: 
                        continue 
                    if new_c > n-1 or new_c < 0: 
                        continue 
                    if visited[new_r][new_c][keys]: 
                        continue 
                    if grid[new_r][new_c] == "#": 
                        continue 
                    if grid[new_r][new_c].isupper(): 
                        idx = all_keys.index(grid[new_r][new_c].lower())
                        if keys & (1 << idx) == 0: 
                            continue 
                    # NOTE 1. where to update visited, inside for, otherwise may have duplicate 
                    # NOTE 2. can only go back after a new key 
                    visited[new_r][new_c][keys] = 1 
                    que.append([new_r, new_c, move+1, keys])

        return -1 

if __name__ == "__main__": 
    s = Solution() 

    # grid = ["@..aA","..B#.","....b"]
    # assert s.shortestPathAllKeys(grid) == 6

    grid = ["@...a",".###A","b.BCc"]
    assert s.shortestPathAllKeys(grid) == 10

    # grid = ["@.a..","###.#","b.A.B"]
    # assert s.shortestPathAllKeys(grid) == 8 