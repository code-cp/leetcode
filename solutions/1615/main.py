from typing import * 

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = {}
        for r in roads: 
            if adj_list.get(r[0], -1) == -1:
                adj_list[r[0]] = []
            if adj_list.get(r[1], -1) == -1:
                adj_list[r[1]] = []
            adj_list[r[0]].append(r[1])
            adj_list[r[1]].append(r[0])
        n = len(adj_list)
        res = 0     
        keys = list(adj_list.keys())
        for i in range(n): 
            for j in range(i+1, n): 
                total = len(adj_list[keys[i]]) + len(adj_list[keys[j]])
                if keys[i] in adj_list[keys[j]]: 
                    total -= 1 
                res = max(res, total)
        return res 