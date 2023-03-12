from typing import * 

# 找最远的nodes
# 从任意node A开始，找最远的node B
# 那么B肯定是最远节点中的一个端点
# 从B出发找最远端点C

from collections import deque 
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:        
        # adjacency list 
        adj = {}
        for edge in edges: 
            if adj.get(edge[0]-1, -1) == -1: 
                adj[edge[0]-1] = []
            if adj.get(edge[1]-1, -1) == -1: 
                adj[edge[1]-1] = []
            # change to 0-indexed 
            adj[edge[0]-1].append(edge[1]-1) 
            adj[edge[1]-1].append(edge[0]-1)

        def bfs(start, dist, allow):
            q = deque()
            q.append(start)
            dist[start] = 0 
            max_dist = 0 
            max_idx = start 
            while len(q) > 0: 
                q_len = len(q)
                for _ in range(q_len): 
                    cur = q.popleft()
                    for nex in adj[cur]:
                        if allow[nex] == 0: 
                            continue 
                        if dist[nex] == -1: 
                            q.append(nex)
                            dist[nex] = dist[cur]+1 
                            if dist[nex] > max_dist:
                                max_dist = dist[nex]
                                max_idx = nex 
            return max_idx 

        # traverse all subtrees 
        count = [0]*n 
        for state in range(1, 1<<n): 
            allow = [0]*n  
            start = -1 
            for i in range(n): 
                if ((state>>i) & 1) == 1: 
                    allow[i] = 1 
                    start = i 
            
            dist = [-1]*n
            end_point1 = bfs(start, dist, allow)
            # check if subtree is connected 
            visited = 0 
            for j in range(n): 
                if dist[j] != -1: 
                    visited += 1 
            if visited != sum(allow): 
                continue 
            dist = [-1]*n
            end_point2 = bfs(end_point1, dist, allow)
            max_diameter = max(dist) 
            count[max_diameter] += 1 
            
        # diameter starts from 1 
        return count[1:] 

        
# if __name__ == "__main__": 
#     s = Solution() 
    
#     assert s.countSubgraphsForEachDiameter()