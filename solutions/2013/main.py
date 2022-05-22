from collections import defaultdict 
from collections import Counter 
from typing import List 

class DetectSquares:

    def __init__(self):
        self.map = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        # map[0][1] += 1
        # defaultdict(<class 'collections.Counter'>, {0: Counter({1: 1})})
        self.map[y][x] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        # check horizontal coordinate
        if not y in self.map:
            return 0
        y_cnt = self.map[y]

        # iterate another horizontal coordinate 
        for col, col_cnt in self.map.items(): 
            # cannot be the same with first horizontal coordinate
            if col != y:
                # square length 
                d = col - y
                res += col_cnt[x] * y_cnt[x + d] * col_cnt[x + d]
                res += col_cnt[x] * y_cnt[x - d] * col_cnt[x - d]

        return res

if __name__ == "__main__": 
# Your DetectSquares object will be instantiated and called as such:
  obj = DetectSquares()
  obj.add([3, 10])
  obj.add([11, 2])
  obj.add([3, 2])
  obj.add([11, 10])
  obj.add([11, 2])
  param = obj.count([11, 10])
  assert param == 2


