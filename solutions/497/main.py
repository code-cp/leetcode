from typing import * 

import random 
# 把每个矩形有多少点记录下来，然后二分找到所在矩形
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.n = len(rects)

        self.rect_pts = []
        count = 0
        for r in self.rects: 
            # NOTE, don't forget +1 
            count += (r[2]-r[0]+1) * (r[3]-r[1]+1)
            self.rect_pts.append(count)
        self.total = count 

    def pick(self) -> List[int]:
        idx = random.randint(1, self.total) 
        l, r = 0, self.n-1 
        while l <= r: 
            mid = (r - l) // 2 + l 
            if self.rect_pts[mid] < idx: 
                l = mid + 1 
            elif self.rect_pts[mid] >= idx: 
                r = mid - 1 
        rect = self.rects[l]
        x = random.randint(rect[0], rect[2]) 
        y = random.randint(rect[1], rect[3]) 
        return [x, y]

if __name__ == "__main__": 
    s = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
    print(s.pick()) 
