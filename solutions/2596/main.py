from typing import * 

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def isValid(pos1, pos2): 
            if abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) == 3: 
                return True 
            return False 
        
        n = len(grid)
        indices = [[] for _ in range(n*n)]
        for i in range(n): 
            for j in range(n): 
                indices[grid[i][j]].append([i, j])

        if indices[0][0] != [0, 0]:
            return False 

        pre = (0, 0)
        for i in range(1, n*n): 
            cur = indices[i][0]
            if not isValid(pre, cur):
                return False 
            pre = cur 
            
        return True 

if __name__ == "__main__":
    s = Solution()
    
    # assert s.checkValidGrid([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]) 
    assert not s.checkValidGrid([[8,3,6],[5,0,1],[2,7,4]]) 