from typing import * 
from collections import deque 
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # utilities 
        m, n = len(matrix), len(matrix[0])
        father = [0]*(m*n)
        for i in range(m): 
            for j in range(n): 
                father[i*n+j] = i*n+j 

        def findFather(x): 
            if father[x] != x: 
                father[x] = findFather(father[x])
            return father[x]

        def union(x, y): 
            x = father[x] 
            y = father[y]
            if x < y: 
                father[y] = x 
            else: 
                father[x] = y 

        # build graph 
        next_graph = [None] * (m*n)
        in_degree = [0] * (m*n)

        for i in range(m):
            row = [] 
            for j in range(n): 
                idx = i*n+j
                row.append((matrix[i][j], idx))
            row.sort()
            
            for j in range(1, n): 
                if row[j][0] == row[j-1][0]: 
                    if findFather(row[j-1][1]) != findFather(row[j][1]):
                        union(row[j-1][1], row[j][1])
                else: 
                    if next_graph[row[j-1][1]] is None: 
                        next_graph[row[j-1][1]] = []
                    next_graph[row[j-1][1]].append(row[j][1])
                    in_degree[row[j][1]] += 1 

        for j in range(n):
            col = [] 
            for i in range(m): 
                idx = i*n+j
                col.append((matrix[i][j], idx))
            col.sort()
            
            for i in range(1, m): 
                if col[i][0] == col[i-1][0]: 
                    if findFather(col[i-1][1]) != findFather(col[i][1]):
                        union(col[i-1][1], col[i][1])
                else: 
                    if next_graph[col[i-1][1]] is None: 
                        next_graph[col[i-1][1]] = []
                    next_graph[col[i-1][1]].append(col[i][1])
                    in_degree[col[i][1]] += 1 

        # build group 
        # key: father idx, value: all members 
        map_group = {}
        for i in range(m): 
            for j in range(n):
                if findFather(i*n+j) not in map_group: 
                    map_group[findFather(i*n+j)] = []
                map_group[findFather(i*n+j)].append(i*n+j)
        for i in range(m): 
            for j in range(n): 
                f = father[i*n+j]
                if f != i*n+j: 
                    in_degree[f] += in_degree[i*n+j]

        # toplogical sort 
        q = deque()
        for i in range(m): 
            for j in range(n): 
                if father[i*n+j] == i*n+j and in_degree[i*n+j] == 0: 
                    q.append(i*n+j)
        rank = 1 
        res = [[0]*n for _ in range(m)]
        while len(q) > 0: 
            l = len(q)
            for i in range(l): 
                cur = q.popleft()
                for e in map_group[cur]: 
                    res[e//n][e%n] = rank 
                for e in map_group[cur]:
                    if next_graph[e] is None:
                        continue  
                    for g in next_graph[e]: 
                        in_degree[father[g]] -= 1 
                        if in_degree[father[g]] == 0: 
                            q.append(father[g])
            rank += 1 

        return res  

if __name__ == "__main__": 
    s = Solution() 

    matrix = [[1,2],[3,4]]
    print(s.matrixRankTransform(matrix))