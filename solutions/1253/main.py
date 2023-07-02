from typing import * 

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        ans = [[0]*n for _ in range(2)]
        for i, c in enumerate(colsum): 
            if c == 2: 
                ans[0][i] = 1 
                ans[1][i] = 1 
                
        upper_sum = sum(ans[0])
        lower_sum = sum(ans[1])
                
        for i, c in enumerate(colsum): 
            if c != 1: 
                continue 
            if upper_sum < upper: 
                ans[0][i] = 1 
                upper_sum += 1 
            elif lower_sum < lower: 
                ans[1][i] = 1 
                lower_sum += 1 
            else: 
                return []
    
        if upper_sum != upper or lower_sum != lower: 
            return []
     
        return ans 

if __name__ == "__main__": 
    s = Solution()
     
    assert s.reconstructMatrix(1,4,[2,1,2,0,0,2])