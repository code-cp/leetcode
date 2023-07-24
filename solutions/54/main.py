class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n
        t, b = 0, m 
        
        while l < r and t < b: 
            # left to right 
            # NOTE, r initially is n, so can use range(l, r)
            for i in range(l, r): 
                ans.append(matrix[t][i])
            t += 1 
            
            # top to down 
            for i in range(t, b): 
                ans.append(matrix[i][r-1])
            r -= 1 
            
            if l >= r or t >= b: 
                break 
            
            # right to left 
            for i in range(r-1, l-1, -1): 
                ans.append(matrix[b-1][i])
            b -= 1 
            
            # bottom to top 
            for i in range(b-1, t-1, -1):
                ans.append(matrix[i][l])  
            l += 1 

        return ans