from typing import * 

from collections import deque 
class Solution:
    def bfs(self, heights, que, scores):
        while len(que) > 0: 
            m = len(que)
            for _ in range(m):
                x, y = que.popleft()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]: 
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n: 
                        continue
                    # NOTE, cannot use visited to keep record 
                    # since the first time we visit, the score may be 0 
                    # and its neighbors will not be added to queue 
                    if scores[nx][ny] == 1:
                        continue 
                    if heights[nx][ny] >= heights[x][y]: 
                        que.append([nx, ny]) 
                        scores[nx][ny] = 1
        return scores

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m, self.n = len(heights), len(heights[0])
        scores1 = [[0] * self.n for _ in range(self.m)]
        scores2 = [[0] * self.n for _ in range(self.m)]

        que = deque()
        for i in range(self.m): 
            que.append([i, 0])
            scores1[i][0] = 1 
        for i in range(self.n): 
            que.append([0, i])
            scores1[0][i] = 1 
        scores1 = self.bfs(heights, que, scores1)

        que = deque() 
        for i in range(self.m):
            que.append([i, self.n-1])
            scores2[i][self.n-1] = 1 
        for i in range(self.n): 
            que.append([self.m-1, i])
            scores2[self.m-1][i] = 1 
        scores2 = self.bfs(heights, que, scores2)

        result = []
        for i in range(self.m): 
            for j in range(self.n): 
                if scores1[i][j] + scores2[i][j] == 2:
                    result.append([i, j])  

        return result

# WRONG version 
# from collections import deque 
# class Solution:
#     def bfs(self, heights, que, scores):
#         while len(que) > 0: 
#             m = len(que)
#             for _ in range(m):
#                 x, y = que.popleft()
#                 for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]: 
#                     nx, ny = x + dx, y + dy
#                     if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n: 
#                         continue
#                     if heights[nx][ny] >= heights[x][y]: 
#                         if not self.visited[nx][ny]:
#                             que.append([nx, ny]) 
#                         scores[nx][ny] = max(scores[x][y], scores[nx][ny]) 
#                     self.visited[nx][ny] = 1 
#         return scores

#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         self.m, self.n = len(heights), len(heights[0])
#         scores1 = [[0] * self.n for _ in range(self.m)]
#         scores2 = [[0] * self.n for _ in range(self.m)]

#         que = deque()
#         self.visited = [[0] * self.n for _ in range(self.m)] 
#         for i in range(self.m): 
#             que.append([i, 0])
#             scores1[i][0] = 1 
#             self.visited[i][0] = 1
#         for i in range(self.n): 
#             que.append([0, i])
#             scores1[0][i] = 1 
#             self.visited[0][i] = 1 
#         scores1 = self.bfs(heights, que, scores1)

#         que = deque()
#         self.visited = [[0] * self.n for _ in range(self.m)] 
#         for i in range(self.m):
#             que.append([i, self.n-1])
#             scores2[i][self.n-1] = 1 
#             self.visited[i][self.n-1] = 1
#         for i in range(self.n): 
#             que.append([self.m-1, i])
#             scores2[self.m-1][i] = 1 
#             self.visited[self.m-1][i] = 1
#         scores2 = self.bfs(heights, que, scores2)

#         result = []
#         for i in range(self.m): 
#             for j in range(self.n): 
#                 if scores1[i][j] + scores2[i][j] == 2:
#                     result.append([i, j])  

#         return result

if __name__ == "__main__": 
    s = Solution() 

    heights = [[2,1],[1,2]]
    result = s.pacificAtlantic(heights) 
    print(result)

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = s.pacificAtlantic(heights)
    print(result)

    heights = [[1,1],[1,1],[1,1]]
    result = s.pacificAtlantic(heights)
    print(result)

    heights = [[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]]
    result = s.pacificAtlantic(heights)
    print(result)

    heights = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
    result = s.pacificAtlantic(heights)
    print(result)