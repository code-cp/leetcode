from typing import * 
from collections import deque 

class Solution:
    def bfs(self, adj_list, patience, root): 
        que = deque()
        one_way = 0 
        distances = [0] * len(adj_list)
        result = 0 
        que.append(root)
        visited = [False] * len(adj_list)
        visited[0] = True 
        # level order traversal
        while len(que) > 0: 
            one_way += 1
            for _ in range(len(que)):
                node = que.popleft() 
                for ne in adj_list[node]:
                    if visited[ne]:
                        continue 
                    dist = self.compute_time(patience[ne], one_way)
                    distances[ne] = dist
                    result = max(dist, result)
                    que.append(ne)
                    visited[ne] = True 
        return result

    def compute_time(self, patience, one_way): 
        two_way = one_way*2
        last_send_time = two_way-1 - (two_way-1) % patience
        total = last_send_time + two_way + 1
        return total

    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        adj_list = [[] for _ in range(n)]
        for e in edges: 
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        root = 0 
        result = self.bfs(adj_list, patience, root)
        return result 

if __name__ == "__main__":
    s = Solution()

    edges = [[0,1],[1,2]]
    patience = [0,2,1]
    result = s.networkBecomesIdle(edges, patience)
    assert result == 8 

    edges = [[0,1],[0,2],[1,2]]
    patience = [0,10,10]
    result = s.networkBecomesIdle(edges, patience)
    assert result == 3

    edges = [[5,7],[15,18],[12,6],[5,1],[11,17],[3,9],[6,11],[14,7],[19,13],[13,3],[4,12],[9,15],[2,10],[18,4],[5,14],[17,5],[16,2],[7,1],[0,16],[10,19],[1,8]]
    patience = [0,2,1,1,1,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1]
    result = s.networkBecomesIdle(edges, patience)
    assert result == 67