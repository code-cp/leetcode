class Solution:
    def backtracking(self, n, k, r, c, t): 
        # base case 
        if r < 0 or r > n-1 or c < 0 or c > n-1: 
            return 0
        if self.memo[r][c][t] != 0: 
            return self.memo[r][c][t]
        if t == k: 
            return 1
        
        # traverse 
        result = 0 
        dirs = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]
        for d in dirs: 
            result += self.backtracking(n, k, r+d[0], c+d[1], t+1)

        self.memo[r][c][t] = result 
        return result

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.memo = [[[0] * (k+1) for _ in range(n)] for _ in range(n)]
        return self.backtracking(n, k, row, column, 0) / (8 ** k)

if __name__ == "__main__": 
    n = 3 
    k = 2 
    row, col = 0, 0
    s = Solution()
    assert s.knightProbability(n, k, row, col) == (4 / (8 ** k))