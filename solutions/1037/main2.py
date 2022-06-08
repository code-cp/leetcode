from typing import * 

class Solution:
    # 分别使用两个点计算向量，随后判断向量叉积是否为 0
    def isBoomerang(self, points: List[List[int]]) -> bool:
        pt2vec = lambda x1, x2: (x1[0] - x2[0], x1[1] - x2[1])

        vec1 = pt2vec(points[0], points[1]) 
        vec2 = pt2vec(points[0], points[2]) 

        return vec1[0] * vec2[1] - vec1[1] * vec2[0] != 0
