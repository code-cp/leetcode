from typing import * 

# ref https://leetcode.cn/problems/frog-position-after-t-seconds/solutions/2281408/dfs-ji-yi-ci-you-qu-de-hack-by-endlessch-jtsr/


# https://leetcode.cn/problems/frog-position-after-t-seconds/solutions/2280227/t-miao-hou-qing-wa-de-wei-zhi-by-leetcod-fea8/

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # 用n+1而不是n，是因为节点是1到n，所以最后一个索引是n
        graph = [[] for _ in range(n+1)]
        for i, j in edges: 
            graph[i].append(j)
            graph[j].append(i)
        visited = [0]*(n+1)
        
        def dfs(i, t): 
            nxt = len(graph[i])
            if i > 1: 
                # 减去一个已经遍历的节点
                nxt -= 1 
            if nxt == 0 or t == 0:
                # 如果后续没有节点，返回0
                # 如果节点等于target，返回1 
                return 1.0 if i == target else 0.0
            visited[i] = 1 
            for j in graph[i]: 
                if not visited[j]: 
                    # 消耗了一个时间单位
                    p = dfs(j, t-1)
                    if p > 0: 
                        # 找到了target
                        # 从当前节点到target节点所在的子树，概率是p / nxt
                        return p / nxt
            return 0.0           
        
        return dfs(1, t)