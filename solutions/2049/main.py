from typing import * 

class Solution:
    def __init__(self): 
        self._max_score = 0 
        self._cnt = 0 
    def dfs(self, adj_list, node):
        n = len(adj_list)
        tree_size = 0 
        score = 1 
        for c in adj_list[node]: 
            sz = self.dfs(adj_list, c)
            score *= sz 
            tree_size += sz 
        tree_size += 1 
        score *= max(n - tree_size, 1)
        if score > self._max_score:
            self._max_score = score 
            self._cnt = 1 
        elif score == self._max_score: 
            self._cnt += 1 
        return tree_size 
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        adj_list = [[] for _ in range(n)]
        for i in range(1, n): 
            adj_list[parents[i]].append(i)
        self.dfs(adj_list, 0)
        return self._cnt 

if __name__ == "__main__":
    s = Solution()

    parents = [-1,2,0,2,0]
    result = s.countHighestScoreNodes(parents)
    assert result == 3 