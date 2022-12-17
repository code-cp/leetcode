from typing import * 

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = [0] * 100005
        for i in range(n): 
            parent[i] = i 

        def findParent(x): 
            if parent[x] != x: 
                parent[x] = findParent(parent[x])
            return parent[x]
        
        def union(x, y):
            x = parent[x]
            y = parent[y]
            if x < y: 
                parent[y] = x 
            else: 
                parent[x] = y  
        
        edgeList.sort(key=lambda x: x[2])

        for i in range(len(queries)): 
            queries[i].append(i)
        queries.sort(key=lambda x: x[2])
        res = [True] * len(queries)

        i = 0 
        for q in queries: 
            while i < len(edgeList) and edgeList[i][2] < q[2]: 
                a = edgeList[i][0]
                b = edgeList[i][1]
                if findParent(a) != findParent(b): 
                    union(a, b)
                i += 1 

            res[q[3]] = findParent(q[0]) == findParent(q[1])

        return res 

if __name__ == "__main__": 
    s = Solution() 

    n = 3 
    edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
    queries = [[0,1,2],[0,2,5]]
    assert s.distanceLimitedPathsExist(n, edgeList, queries) == [False, True]