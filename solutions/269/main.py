from typing import * 

from collections import defaultdict 
from itertools import pairwise
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def postorder_dfs_check_loop(adj, visited, res, node): 
            # base case 
            if node in visited: 
                # check loop 
                return visited[node]

            visited[node] = True 

            for neighbor in adj[node]:
                if postorder_dfs_check_loop(adj, visited, res, neighbor): 
                    return True  

            visited[node] = False 
            # post order dfs 
            res.append(node) 

        # create adjacency list 
        adj_list = {} 
        for w in words: 
            for c in w: 
                adj_list[c] = set()
        
        # build adjacency 
        for w1, w2 in pairwise(words): 
            min_len = min(len(w1), len(w2)) 
            # check for violation 
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: 
                return "" 
            for j in range(min_len): 
                if w1[j] != w2[j]: 
                    adj_list[w1[j]].add(w2[j]) 
                    break 
        
        # dfs 
        visited = defaultdict(str)  
        res = []
        for node in adj_list: 
            if postorder_dfs_check_loop(adj_list, visited, res, node): 
                return "" 

        return "".join(res[::-1]) 

if __name__ == "__main__": 
    s = Solution() 

    words = ["wrt","wrf","er","ett","rftt"]
    assert s.alienOrder(words) == "wertf" 