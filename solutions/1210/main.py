# ref https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/solutions/2093126/huan-zai-if-elseyi-ge-xun-huan-chu-li-li-tw8b/

# XOR table 
#   0 0 = 0
#   1 0 = 1
#   0 1 = 1
#   1 1 = 0

from typing import * 
from collections import deque 
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[[0]*2 for _ in range(n)] for _ in range(n)]

        def checkValid(state, d): 
            tail_pos = (state[0], state[1])
            # NOTE state[1]+state[2]^1 won't work
            head_pos = (state[0]+state[2], state[1]+(state[2]^1))
            # check border 
            if head_pos[0] >= n or head_pos[1] >= n: 
                return False 
            
            # check obstacle 
            if (grid[tail_pos[0]][tail_pos[1]] == 1 
                or grid[head_pos[0]][head_pos[1]] == 1):
                return False 

            # check rotate 
            if d[2] == 1: 
                if grid[tail_pos[0]+1][tail_pos[1]+1] == 1:
                    return False 
       
            if visited[state[0]][state[1]][state[2]] == 1: 
                return False 

            return True 

        q = deque()
        q.append((0,0,0))
        visited[0][0][0] = 1 
        # NOTE horizontal move means the whole body moves horizontally
        dirs = [(1,0,0),(0,1,0),(0,0,1)]
        dis = 0 
        target = (n-1, n-2, 0)
        while len(q) > 0: 
            q_size = len(q)
            for _ in range(q_size): 
                state = q.popleft()
                if state == target: 
                    return dis
                # print(f"{state=}")
                for d in dirs: 
                    new_state = (state[0]+d[0], state[1]+d[1], state[2]^d[2])
                    if checkValid(new_state, d):
                        visited[new_state[0]][new_state[1]][new_state[2]] = 1 
                        q.append(new_state)
                        # print(f"{new_state=}")
            dis += 1 

        return -1 

if __name__ == "__main__": 
    s = Solution() 

    grid = [[0,0,0,0,0,1],
            [1,1,0,0,1,0],
            [0,0,0,0,1,1],
            [0,0,1,0,1,0],
            [0,1,1,0,0,0],
            [0,1,1,0,0,0]]
    assert s.minimumMoves(grid) == 11 