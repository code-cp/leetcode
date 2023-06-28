class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        circle_x1 = xCenter - radius 
        circle_y1 = yCenter - radius 
        circle_x2 = xCenter + radius 
        circle_y2 = xCenter + radius 
        
        for i in range(circle_x1, circle_x2+1): 
            for j in range(circle_y1, circle_y2+1): 
                if (i-xCenter)**2 + (j-yCenter)**2 > radius**2:
                    continue  
                if i < x1 or i > x2: 
                    continue 
                if j < y1 or j > y2: 
                    continue 
                return True 
            
        return False 

if __name__ == "__main__": 
    s = Solution()
    
    assert s.checkOverlap(1,0,0,1,-1,3,1)
                