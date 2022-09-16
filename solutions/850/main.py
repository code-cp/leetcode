from typing import * 

# 二维差分数组
class DiffMat: 
    def __init__(self, m, n):
        self._m, self._n = m, n  
        self._diff = [[0] * self._n for _ in range(self._m)]
        self.res = [[0] * self._n for _ in range(self._m)]

    @property 
    def diff(self):
        return self._diff 

    @diff.setter 
    def diff(self, set_val): 
        x0, y0, x1, y1, val = set_val
        self._diff[x0][y0] += val 
        self._diff[x0][y1+1] -= val 
        self._diff[x1+1][y0] -= val 
        self._diff[x1+1][y1+1] += val 

    def convert(self): 
        self.res[0][0] = self._diff[0][0]
        for i in range(self._m): 
            for j in range(self._n): 
                a = 0 if i == 0 else self.res[i-1][j] 
                b = 0 if j == 0 else self.res[i][j-1]
                c = 0 if (i == 0 and j == 0) else self.res[i-1][j-1]
                self.res[i][j] = a + b - c + self._diff[i][j]; 

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # 离散化
        point_x = set()
        point_y = set()

        for rect in rectangles: 
            point_x.add(rect[0])
            point_y.add(rect[1])
            point_x.add(rect[2])
            point_y.add(rect[3])

        row = sorted(list(point_x))
        col = sorted(list(point_y))

        m, n = len(row), len(col)

        x_to_idx = dict()
        y_to_idx = dict()

        for i in range(m): 
            x_to_idx[row[i]] = i 
        for j in range(n): 
            y_to_idx[col[j]] = j 

        dm = DiffMat(m, n) 
        
        for rect in rectangles: 
            x0 = x_to_idx[rect[0]]
            y0 = y_to_idx[rect[1]]
            # 像素不是坐标，需要-1
            x1 = x_to_idx[rect[2]]-1
            y1 = y_to_idx[rect[3]]-1
            dm.diff = (x0, y0, x1, y1, 1)

        dm.convert()
        CONST = 1e9 + 7
        area = 0 
        # 1 <= rectangles.length <= 200
        for i in range(m): 
            for j in range(n): 
                if dm.res[i][j] > 0: 
                    dx = row[i+1] - row[i]
                    dy = col[j+1] - col[j]
                    area += (dx * dy) % CONST
                    area %= CONST
        
        return int(area) 

if __name__ == "__main__": 
    s = Solution() 

    rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    assert s.rectangleArea(rectangles) == 6 

