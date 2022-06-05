from typing import * 

from random import uniform
import math 
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius 
        self.cx = x_center 
        self.cy = y_center 

    def randPoint(self) -> List[float]:
        # 注意半径的随机不能从0到r，要从0到r^2随机后开方，因为是面积微分的随机，不是半径微分的随机
        # or 在圆的外接正方形内随机，判断在圆外部的时候重新随机即可。这样概率不会出问题。 
        r2 = uniform(0.0, self.r ** 2)
        r = math.sqrt(r2)
        phi = uniform(-math.pi, math.pi) 
        x = r * math.cos(phi) + self.cx 
        y = r * math.sin(phi) + self.cy 
        return [x, y]


if __name__ == '__main__':
    radius = 5 
    x_center = 0 
    y_center = 0 
    obj = Solution(radius, x_center, y_center)
    param_1 = obj.randPoint()
    print(param_1)