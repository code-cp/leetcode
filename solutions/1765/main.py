from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # initialize
        row, col = len(isWater), len(isWater[0])
        ans = [[-1] * col for _ in range(row)]
        que = deque(maxlen=row*col)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        # push water cells in queue
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    que.append((i, j))
                    ans[i][j] = 0
        # bfs
        h = 1
        while len(que) > 0:
            q_size = len(que)
            while q_size > 0:
                x, y = que.popleft()
                for d in dirs:
                    nx, ny = x+d[0], y+d[1]
                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        continue
                    if ans[nx][ny] == -1:
                        ans[nx][ny] = h
                        que.append((nx, ny))
                q_size -= 1
            h += 1
        return ans

if __name__ == "__main__": 
    isWater = [[0,1],[0,0]]
    s = Solution()
    print(s.highestPeak(isWater))
