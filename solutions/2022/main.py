from typing import List 

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        result = [[0]*n for _ in range(m)]
        for i in range(m):
            result[i] = original[i*n:(i+1)*n]
        return result

if __name__ == "__main__": 
    original = [1,2,3,4] 
    m = 2 
    n = 2
    s = Solution()
    result = [[1,2],[3,4]]
    assert s.construct2DArray(original, m, n) == result
