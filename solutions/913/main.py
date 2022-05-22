from typing import List 

class Solution:
    @staticmethod
    def findPrevState(graph, state):
        result = []
        j, t, m = state
        if m == 1:
            for tNeighbor in graph[t]:
                if tNeighbor == 0:
                    continue
                # tom moves from tNeighbor to t
                jPre, tPre, mPre = j, tNeighbor, 2
                result.append([jPre, tPre, mPre])
        elif m == 2:
            for jNeighbor in graph[j]:
                # jerry moves from jNeighbor to j
                jPre, tPre, mPre = jNeighbor, t, 1
                result.append([jPre, tPre, mPre])
        return result
    @staticmethod
    def isDoomed(graph, result, state):
        j, t, m = state
        if m == 1:
            for jNeighbor in graph[j]:
                # jerry can win or draw in next move
                if result[jNeighbor][t][2] != 2:
                    return False
        elif m == 2:
            for tNeighbor in graph[t]:
                if tNeighbor == 0:
                    continue
                # tom can win or draw in next move
                if result[j][tNeighbor][1] != 1:
                    return False
        return True
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        # 0: undefied = draw
        # 1: jerry move/win
        # 2: tom move/win
        result = [[[0]*3 for _ in range(N)] for _ in range(N)]
        que = []
        # start from initial states
        for i in range(1, 3):
            for j in range(1, N):
                # jerry always win
                result[0][j][i] = 1
                que.append([0, j, i])
                # tom always win
                result[j][j][i] = 2
                que.append([j, j, i])
        # traverse BFS
        while len(que) > 0:
            state = que[0]
            que.pop(0)
            j, t, m = state
            for preState in self.findPrevState(graph, state):
                jPre, tPre, mPre = preState
                # already processed
                if result[jPre][tPre][mPre] != 0:
                    continue
                # wins in previous state
                # 3-m means current move and result are different, if same then neither tom nor jerry will arrive at this state
                if result[j][t][m] == 3-m:
                    result[jPre][tPre][mPre] = mPre
                    que.append(preState)
                # cannot win any way, so will arrive at this state
                elif self.isDoomed(graph, result, preState):
                    result[jPre][tPre][mPre] = 3-mPre
                    que.append(preState)
        return result[1][2][1]

if __name__ == "__main__": 
    graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    s = Solution()
    assert s.catMouseGame(graph) == 0
