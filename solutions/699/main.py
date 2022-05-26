from bz2 import compress
from typing import * 

class SegmentTree(): 
    def __init__(self, N, update_fn, query_fn): 
        self.N = N 
        # H is the smallest power of 2 that 2^H >= N 
        self.H = 1 
        while 1 << self.H < N:
            self.H += 1 

        self.update_fn = update_fn 
        self.query_fn = query_fn 
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N 

    def _apply(self, x, val): 
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N: 
            self.lazy[x] = self.update_fn(self.lazy[x], val)
        
    def _pull(self, x): 
        while x > 1: 
            x //= 2 
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[2*x + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])
    
    def _push(self, x): 
        for h in range(self.H, 0, -1): 
            y = x >> h 
            if self.lazy[y]: 
                self._apply(y*2, self.lazy[y])
                self._apply(y*2 + 1, self.lazy[y])
                self.lazy[y] = 0 
    
    def update(self, L, R, h): 
        L += self.N 
        R += self.N 
        L0, R0 = L, R 
        while L <= R: 
            if L & 1: 
                self._apply(L, h) 
                L += 1 
            if R & 1 == 0: 
                self._apply(R, h) 
                R -= 1 
            L //= 2
            R //= 2
        self._pull(L0)
        self._pull(R0) 

    def query(self, L, R): 
        L += self.N 
        R += self.N 
        self._push(L) 
        self._push(R) 
        ans = 0 
        while L <= R: 
            if L & 1: 
                ans = self.query_fn(ans, self.tree[L])
                L += 1 
            if R & 1 == 0: 
                ans = self.query_fn(ans, self.tree[R]) 
                R -= 1
            L //= 2 
            R //= 2 
        return ans 
            

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        def compress(positions): 
            coords = set()
            for left, size in positions:
                coords.add(left)
                coords.add(left + size - 1)
            index = {x: i for i, x in enumerate(sorted(coords))}
            return index 

        index = compress(positions) 
        tree = SegmentTree(len(index), max, max)
        best = 0 
        ans = []
        for left, size in positions: 
            L, R = index[left], index[left + size - 1] 
            h = tree.query(L, R) + size 
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)
        return ans 

if __name__ == "__main__": 
    s = Solution()

    assert s.fallingSquares([[1,2],[2,3],[6,1]]) == [2,5,5] 