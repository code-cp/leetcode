from typing import * 

class Solution:
    def traverse(self, start, n):
        result = [] 
        for i in range(10): 
            j = start*10 + i 
            if j > n: 
                return result 
            # visit 
            result += [j] 
            # L, R 
            result += self.traverse(j, n)
        return result 
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        if n < 10: 
            return list(range(1, n+1))
        for i in range(1, 10): 
            # visit 
            result += [i]
            # L, R
            result += self.traverse(i, n)
        return result 

if __name__ == "__main__": 
    solution = Solution()

    n = 13 
    result = solution.lexicalOrder(n) 
    assert result == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9] 