from typing import List 

class Solution:
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # NOTE, need to use set instead of list, otherwise list will TLE
        self.visited = set()
    @staticmethod
    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    def dfs(self, source, target, cur):
        # base case
        if cur == target:
            return True
        if self.manhattan(source, cur) > 200:
            return True
        # NOTE, list is not hashable, tuple is
        cur_tuple = (cur[0], cur[1])
        self.visited.add(cur_tuple)
        for d in self.dirs:
            new_cur = [0]*2
            new_cur[0] = cur[0] + d[0]
            new_cur[1] = cur[1] + d[1]
            if new_cur[0] >= 0 and new_cur[0] < 1e6 and new_cur[1] >= 0 and new_cur[1] < 1e6:
                if new_cur not in self.blocked:
                    new_cur_tuple = (new_cur[0], new_cur[1])
                    if new_cur_tuple not in self.visited:
                        if self.dfs(source, target, new_cur):
                            return True
        return False
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        self.blocked = blocked
        if self.dfs(source, target, source):
            self.visited.clear()
            if self.dfs(target, source, target):
                return True
        return False

if __name__ == "__main__": 
    blocked = [[0,3],[1,0],[1,1],[1,2],[1,3]]
    source = [0,0]
    target = [0,2]
    s = Solution()
    assert s.isEscapePossible(blocked, source, target)
