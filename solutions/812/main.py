from typing import * 

class Solution:
    def findConvexHull(self, points): 
        # utility functions 
        def crossProduct(a, b): 
            return a[0] * b[1] - a[1] * b[0]
        def findNextVertex(a, b, c): 
            return crossProduct([c[0] - a[0], c[1] - a[1]], [b[0] - a[0], b[1] - a[1]]) 

        n = len(points)

        if n < 4: 
            return points

        leftMostVertex = 0 
        for i, (x, _) in enumerate(points): 
            if x < points[leftMostVertex][0]: 
                leftMostVertex = i 

        ans = []
        addedVertex = []

        curVertex = leftMostVertex 
        while True: 
            candVertex = (curVertex + 1) % n   
            for i in range(n): 
                if findNextVertex(points[curVertex], points[candVertex], points[i]) > 0: 
                    candVertex = i 

            for i in range(n): 
                if findNextVertex(points[curVertex], points[candVertex], points[i]) == 0: 
                    if i not in addedVertex:
                        ans.append(points[i]) 
                        addedVertex.append(i)

            curVertex = candVertex 

            if curVertex == leftMostVertex: 
                break 

        return ans 

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = lambda x1, x2, x3: 0.5 * abs(x1[0]*(x2[1]-x3[1]) + x2[0]*(x3[1]-x1[1]) + x3[0]*(x1[1]-x2[1]))

        hull = self.findConvexHull(points) 
        n = len(hull)

        # ref https://stackoverflow.com/a/1621913
        a = 0 
        maxArea = 0  
        while True: 
            # loop a 
            c = a+2 
            for b in range(a+1, n-1): 
                # loop b 
                while area(hull[a], hull[b], hull[c]) < area(hull[a], hull[b], hull[(c+1)%n]):      
                    # loop c 
                    c = (c+1)%n        
                curArea = area(hull[a], hull[b], hull[c])
                if curArea > maxArea:
                    maxArea = curArea 

            a = (a+1)%n 
            if a == 0: 
                break 

        return maxArea

if __name__ == "__main__": 
    s = Solution() 

    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    assert s.largestTriangleArea(points) == 2.0 

    points = [[1,0],[0,0],[0,1]]
    assert s.largestTriangleArea(points) == 0.5  

    points = [[-19,30],[-22,21],[-30,5],[-8,2],[-38,40],[-11,22],[-43,28],[1,-11],[29,-4],[31,-41],[10,41],[49,-40],[38,25],[17,-2],[-37,34],[43,17],[10,-39],[25,10],[10,43],[27,-44]]
    assert s.largestTriangleArea(points) == 2811.0 

    points = [[25,30],[48,-27],[-44,29],[-37,-21],[38,33],[-43,-13],[21,-24],[17,-31],[-16,-1],[-25,18],[4,0],[-4,19],[-23,45],[18,35],[48,-11],[-39,-40],[-35,-4],[41,-15],[30,50],[28,-22],[-17,-18],[11,7],[-8,28],[-10,-33],[28,-46],[22,18],[17,26],[-22,50],[17,-38],[20,-23],[-19,4],[-49,4],[35,-22],[-32,23],[-18,-41],[21,13],[4,48],[-22,-46],[3,-30],[38,26]]
    assert s.largestTriangleArea(points) == 3804.5 