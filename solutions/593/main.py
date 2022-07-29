from typing import * 

import math 
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def crossProduct(a, b): 
            return a[0] * b[1] - a[1] * b[0]
        def mag(a): 
            return math.sqrt(a[0] ** 2 + a[1] ** 2)
        def checkPerp(a, b): 
            return abs(abs(crossProduct(a, b)) - mag(a) * mag(b)) < 1e-3 
        def sub(a, b):
            return [a[0]-b[0], a[1]-b[1]]
        def checkEqual(x, y):
            if x[0] == y[0] and x[1] == y[1]:
                return True 
            return False 

        p = [p1, p2, p3, p4]
        p.sort(key=lambda i: (i[0], i[1]))
        p1, p2, p3, p4 = p 

        if checkEqual(p1, p2) or checkEqual(p2, p3) or checkEqual(p3, p4):
            return False 
        if mag(sub(p1, p2)) != mag(sub(p1, p3)):
            return False 
        if not checkPerp(sub(p1, p2), sub(p1, p3)):
            return False 
        if not checkPerp(sub(p3, p4), sub(p2, p4)):
            return False 

        return True 

if __name__ == "__main__": 
    s = Solution()

    # p1 = [0,0]
    # p2 = [1,1]
    # p3 = [1,0]
    # p4 = [0,1]
    # assert s.validSquare(p1, p2, p3, p4)

    # p1 = [0,0]
    # p2 = [1,1]
    # p3 = [1,0]
    # p4 = [0,12]
    # assert not s.validSquare(p1, p2, p3, p4)

    p1 = [1,0]
    p2 = [-1,0]
    p3 = [0,1]
    p4 = [0,-1]
    assert s.validSquare(p1, p2, p3, p4)