from typing import * 

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        diss = {}
        for d in dislikes: 
            if d[0]-1 not in diss: 
                diss[d[0]-1] = []
            if d[1]-1 not in diss: 
                diss[d[1]-1] = []
            diss[d[0]-1].append(d[1]-1)
            diss[d[1]-1].append(d[0]-1)
        if len(diss) == 0:
            return True 

        colors = [-1] * n 

        def dfs(cur, color): 
            colors[cur] = color
            # if no opponents just return true 
            if cur not in diss: 
                return True 
            for neighbor in diss[cur]: 
                if colors[neighbor] == color: 
                    # conflict 
                    return False 
                elif colors[neighbor] == -1 and not dfs(neighbor, 1-color): 
                    return False 
            return True 

        for i in range(n): 
            # by default color is 0
            if colors[i] == -1 and not dfs(i, 0):
                return False 
        return True 

            

if __name__ == "__main__": 
    s = Solution()

    n = 10
    dislikes = [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]
    assert s.possibleBipartition(n, dislikes)

    n = 1
    dislikes = []
    assert s.possibleBipartition(n, dislikes)

    n = 50
    dislikes = [[26,47],[39,46],[11,28],[9,41],[23,41],[2,22],[18,19],[23,26],[2,5],[19,40],[2,48],[14,31],[13,45],[4,19],[1,45],[14,18],[11,22],[5,47],[11,27],[33,39],[2,35],[29,47],[15,49],[12,34],[15,34],[13,35],[36,50],[10,13],[14,24],[13,37],[27,39],[6,23],[7,22],[30,39],[2,17],[36,41],[34,41],[24,49],[18,36],[24,36],[13,38],[27,34],[3,36],[34,48],[23,37],[16,47],[2,18],[13,26],[3,11],[1,15],[26,39],[14,33],[26,49],[25,47],[15,36],[13,41],[9,25],[23,50],[39,41],[29,49],[2,38],[7,15],[11,31],[9,40],[7,24],[6,49],[13,16],[13,29],[11,46],[9,50],[19,43],[11,48],[46,49],[28,49],[6,11],[9,17],[33,49],[32,39],[16,23],[23,27],[7,40],[14,40],[4,11],[9,10],[38,39],[19,38],[14,25],[16,36],[32,49],[22,36],[21,36],[2,44],[8,39],[23,33],[9,38],[16,39],[19,35],[36,42],[34,38],[1,21],[5,13],[19,37],[14,26],[24,47],[1,42],[15,19],[5,23],[7,20],[6,36],[29,39],[9,33],[41,47],[5,49],[7,50],[14,38],[4,13],[13,40],[19,32],[1,32],[39,40],[48,49],[12,14],[7,27],[5,39],[1,4],[36,46],[39,45],[13,28],[36,44],[1,22],[19,42],[35,49],[9,24],[19,31],[44,47],[14,16],[47,48],[22,47],[7,30],[13,18],[7,43],[14,41],[13,31],[1,17],[12,47],[14,30],[13,44],[37,49],[39,50],[5,19],[45,49],[2,45],[1,29],[7,29],[3,14],[2,26],[23,30],[14,42],[4,9],[10,49],[37,39],[18,49],[25,39],[20,39],[19,25],[27,36],[1,41],[4,34],[30,34],[35,47],[21,23],[14,48],[13,24],[11,37],[34,40],[23,29],[7,46],[18,39],[3,19],[9,31],[39,43],[38,49],[20,36],[19,20],[15,23],[6,19],[9,46],[7,26],[14,44],[1,30],[9,35],[16,34],[13,27],[1,8],[7,48],[19,45],[2,15],[22,39],[1,16]]
    assert s.possibleBipartition(n, dislikes)

    n = 3
    dislikes = [[1,2],[1,3],[2,3]]
    assert not s.possibleBipartition(n, dislikes)

    n = 4
    dislikes = [[1,2],[1,3],[2,4]]
    assert s.possibleBipartition(n, dislikes)