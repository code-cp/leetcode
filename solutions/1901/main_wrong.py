from typing import * 

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0]) 
        
        for i in range(m):
            l, r = 0, n-1 
            while l <= r: 
                mid = ((r-l) >> 1) + l 
                if mid == n-1: 
                    break 
                if mid == 0 and n == 1: 
                    break 
                if mid == 0 and n > 1 and mat[i][mid] > mat[i][mid+1]: 
                    break 
                if mat[i][mid] > mat[i][mid-1] and mat[i][mid] > mat[i][mid+1]: 
                    break 
                if mat[i][mid] < mat[i][mid+1]: 
                    l = mid + 1 
                else: 
                    r = mid - 1 

            ans = [i, mid]
            if i == 0: 
                if m == 1: 
                    return ans
                if mat[i][mid] > mat[i+1][mid]:
                    return ans
            if i == m-1: 
                if m == 1: 
                    return ans
                if mat[i][mid] > mat[i-1][mid]: 
                    return ans
            if mat[i][mid] < mat[i-1][mid]:
                continue 
            if mat[i][mid] < mat[i+1][mid]: 
                continue 
            return ans 

if __name__ == "__main__": 
    s = Solution()
    
    # s.findPeakGrid([[1,4],[3,2]])   
    # s.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]])

    # matrix = [
    #     [25, 37, 23, 37, 19],
    #     [45, 19, 2, 43, 26],
    #     [18, 1, 37, 44, 50]
    # ]
    # s.findPeakGrid(matrix)
    
    # 无法处理这种情况
    # 第一行找到了3，但实际应该是7  
    # 53 / 55 个通过的测试用例
    s.findPeakGrid([[7,2,3,1,2],[6,5,4,2,1]])       