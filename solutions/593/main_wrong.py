from typing import * 

# this is wrong since the square may not be aligned with the axis 
import math 
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        checkEqual = lambda x, y: x == y
        def crossProduct(a, b): 
            return a[0] * b[1] - a[1] * b[0]
        def mag(a): 
            return math.sqrt(a[0] ** 2 + a[1] ** 2)

        p = [p1, p2, p3, p4]
        p.sort(key=lambda i: (i[0], i[1]))

        if not checkEqual(p[0][0], p[1][0]) or not checkEqual(p[2][0], p[3][0]):
            return False 
        if not checkEqual(p[0][1], p[2][1]) or not checkEqual(p[1][1], p[3][1]):
            return False 
        
        if checkEqual(p[1][0], p[2][0]) or checkEqual(p[0][1], p[1][1]):
            return False 

        if not checkEqual(p[2][0] - p[0][0], p[1][1] - p[0][1]):
            return False 

        return True 

if __name__ == "__main__": 
    s = Solution()

    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]
    assert s.validSquare(p1, p2, p3, p4)

    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,12]
    assert not s.validSquare(p1, p2, p3, p4)

    p1 = [1,0]
    p2 = [-1,0]
    p3 = [0,1]
    p4 = [0,-1]
    assert s.validSquare(p1, p2, p3, p4)