from typing import * 

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0]) 
        
        def checkPeak(i, j):
            # 只需要检查同一列的方向
            if m == 1: 
                return True 
            if i == 0: 
                if mat[i][j] > mat[i+1][j]: 
                    return True 
            if i == m-1: 
                if mat[i][j] > mat[i-1][j]: 
                    return True 
            if mat[i][j] > mat[i-1][j] and mat[i][j] > mat[i+1][j]: 
                return True 
            return False 
        
        # 爬坡
        l, r = 0, m-1 
        while l <= r: 
            mid = ((r-l) >> 1) + l 
            # 不是爬坡法，而是找最大值
            j = mat[mid].index(max(mat[mid]))
            if checkPeak(mid, j):
                return [mid, j]
            if mid == m-1: 
                r = mid - 1 
                continue 
            if mat[mid][j] < mat[mid+1][j]: 
                l = mid + 1
            else:
                r = mid - 1

        raise NotImplementedError("Shout not reach here!")

if __name__ == "__main__": 
    s = Solution()
    s.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]])
    
    # matrix = [
    #     [30, 41, 24, 11, 24],
    #     [23, 14, 43, 18, 45],
    #     [44, 42, 5, 39, 41],
    #     [11, 35, 47, 16, 11],
    #     [30, 25, 18, 41, 45]
    # ]
    # s.findPeakGrid(matrix)
            