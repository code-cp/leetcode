from typing import * 
from collections import deque 

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        
        # adjacency list 
        nex = [set() for _ in range(n)]
        
        # degree for each node 
        degree = [0]*n 
        for e in edges: 
            a, b = e[0], e[1] 
            nex[a].add(b)
            nex[b].add(a) 
            degree[a] += 1 
            degree[b] += 1 
            
        # prune the useless nodes 
        # whose degree is 1 and coin value is 0 
        deleted = [0]*n 
        q = deque()
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                q.append(i)
        while len(q) > 0: 
            q_len = len(q)
            for _ in range(q_len): 
                cur = q.popleft()
                deleted[cur] = 1 
                cur_nex = nex[cur].copy()
                for nx in cur_nex: 
                    # update the info in adjacency list 
                    degree[nx] -= 1 
                    nex[nx].remove(cur)
                    if degree[nx] == 1 and coins[nx] == 0: 
                        q.append(nx)
                        
        # topological sort
        # erase the degree 1 nodes twice is easier to understand   
        # https://leetcode.cn/problems/collect-coins-in-a-tree/solutions/2451073/shou-ji-shu-zhong-jin-bi-by-leetcode-sol-kaah/?envType=daily-question&envId=2023-09-21
        depth = [-1]*n 
        for i in range(n): 
            if degree[i] == 1 and deleted[i] == 0: 
                q.append(i)
                depth[i] = 1 
        while len(q) > 0: 
            q_len = len(q)
            for _ in range(q_len): 
                cur = q.popleft()
                cur_nex = nex[cur].copy()
                for nx in cur_nex: 
                    degree[nx] -= 1 
                    nex[nx].remove(cur)
                    depth[nx] = max(depth[nx], depth[cur]+1)
                    if degree[nx] == 1: 
                        q.append(nx)

        
        res = 0 
        for i in range(n):
            # Collect all the coins that are at a distance of at most 2 from the current vertex
            res += 1 if depth[i] >= 3 else 0 
        
        if res >= 1: 
            # go back to the initial vertex so *2 
            return (res-1)*2 
        else: 
            # can collect all coins, no need to move at all 
            return 0 

            
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.collectTheCoins([1,0,0,0,0,1], [[0,1],[1,2],[2,3],[3,4],[4,5]]) == 2