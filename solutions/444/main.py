from typing import * 

from collections import defaultdict, deque 
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # build graph 
        nodes = set(v for seq in sequences for v in seq)
        graph = defaultdict(list)
        in_degrees = {v: 0 for v in nodes}
        for seq in sequences: 
            for i in range(len(seq)-1): 
                x, y = seq[i], seq[i+1]
                graph[x].append(y)
                in_degrees[y] += 1 
        # bfs 
        res = []
        bfs = deque([k for k, v in in_degrees.items() if v == 0])
        while len(bfs) > 0: 
            if len(bfs) != 1:
                # path is not unique  
                return False 
            cur = bfs.popleft()
            res.append(cur)
            for nxt in graph[cur]: 
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0: 
                    bfs.append(nxt)
        return sum(in_degrees.values()) == 0 and res == nums 

if __name__ == "__main__": 
    s = Solution()

    nums = [1,2,3] 
    sequences = [[1,2],[1,3]]
    assert not s.sequenceReconstruction(nums, sequences) 