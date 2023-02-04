from typing import * 

from collections import deque 
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = {}
        for r in redEdges: 
            if red.get(r[0], -1) == -1: 
                red[r[0]] = []
            red[r[0]].append(r[1])
        blue = {}
        for b in blueEdges:
            if blue.get(b[0], -1) == -1: 
                blue[b[0]] = []
            blue[b[0]].append(b[1])

        res = [-1]*n
        visited = [[0]*2 for _ in range(n)] 

        q = deque()
        # node idx, color 
        # 0 is red, 1 is blue 
        q.append((0, 0))
        q.append((0, 1))
        path = 0 
        while len(q) > 0: 
            q_size = len(q)
            for _ in range(q_size): 
                (node, color) = q.popleft()
                res[node] = path if res[node] == -1 else min(res[node], path)
                visited[node][color] = 1 
                next_color = 1-color 
                if next_color == 0: 
                    next_nodes = red.get(node, [])
                else: 
                    next_nodes = blue.get(node, [])
                if len(next_nodes) > 0: 
                    for nn in next_nodes:
                        if visited[nn][next_color] != 1:
                            q.append((nn, next_color))
            path += 1 

        return res 
        
if __name__ == "__main__": 
    s = Solution() 

    n = 6
    redEdges = [[4,1],[3,5],[5,2],[1,4],[4,2],[0,0],[2,0],[1,1]]
    blueEdges = [[5,5],[5,0],[4,4],[0,3],[1,0]]
    assert s.shortestAlternatingPaths(n, redEdges, blueEdges) == [0,-1,4,1,-1,2]

    # n = 3
    # redEdges = [[0,1],[0,2]]
    # blueEdges = [[1,0]]
    # assert s.shortestAlternatingPaths(n, redEdges, blueEdges) == [0,1,1]

    # n = 3
    # redEdges = [[0,1],[1,2]]
    # blueEdges = []
    # assert s.shortestAlternatingPaths(n, redEdges, blueEdges) == [0,1,-1]