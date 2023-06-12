from typing import * 
import heapq 
import math 
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = {}
        modify = [[0]*n for _ in range(n)]
        for e in edges: 
            a, b, w = e[0], e[1], e[2]
            if w == -1:
                modify[a][b] = 1 
                modify[b][a] = 1  
                w = 1
            if a not in graph: 
                graph[a] = {}
            graph[a][b] = w 
            if b not in graph: 
                graph[b] = {} 
            graph[b][a] = w 
        
        # dijstra for dist to destination 
        inf = float("inf")
        hq = []
        heapq.heappush(hq, (0, destination))
        dist_to_destination = [inf]*n 
        while len(hq) > 0: 
            d, cur = heapq.heappop(hq)
            if math.isfinite(dist_to_destination[cur]):
                continue 
            # mark the shortest dist 
            dist_to_destination[cur] = d 
            for (nxt, w) in graph[cur].items(): 
                if math.isfinite(dist_to_destination[nxt]):
                    continue 
                heapq.heappush(hq, (d+w, nxt))

        dist_to_source = [inf]*n 
        heapq.heappush(hq, (0, source))
        while len(hq) > 0: 
            d, cur = heapq.heappop(hq)
            if math.isfinite(dist_to_source[cur]):
                continue 
            dist_to_source[cur] = d 
            if cur == destination and d != target: 
                return []
            for (nxt, w) in graph[cur].items(): 
                if math.isfinite(dist_to_source[nxt]): 
                    continue 
                if modify[cur][nxt] == 1 and \
                    (dist_to_source[cur]+w+dist_to_destination[nxt]) < target: 
                        w = target - dist_to_source[cur] - dist_to_destination[nxt]
                        graph[cur][nxt] = w
                        graph[nxt][cur] = w 
                heapq.heappush(hq, (d+w, nxt))
                
        for e in edges: 
            a, b = e[0], e[1]
            e[2] = graph[a][b]
            
        return edges         
        
if __name__ == "__main__": 
    s = Solution() 

    n = 5
    edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
    source = 0
    destination = 1
    target = 5
    print(s.modifiedGraphEdges(n, edges, source, destination, target)) 
    
    # n = 3
    # edges = [[0,1,-1],[0,2,5]]
    # source = 0
    # destination = 2
    # target = 6
    # assert s.modifiedGraphEdges(n, edges, source, destination, target) == []