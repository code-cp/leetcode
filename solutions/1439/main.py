from typing import * 
import heapq 
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        
        array_sum = [0]
        for r in range(m):
            temp_sum = [] 
            for j in array_sum: 
                for c in range(n): 
                    temp_sum.append(j+mat[r][c])
            temp_sum.sort()
            temp_sum = temp_sum[:k]
            array_sum = [x for x in temp_sum]
        
        return array_sum[k-1]

if __name__ == "__main__": 
    s = Solution() 
    
    assert s.kthSmallest([[1,3,11],[2,4,6]], 5) == 7 