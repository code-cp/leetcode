from typing import List 

class Solution:
    def __init__(self):
        self.result = []
    @staticmethod
    def isValid(chessboard, n, row, col):
        # check col
        for i in range(row):
            if (chessboard[i][col] == 'Q'):
                return False
        # check row
        # skip, since in level traversal we only place one Q
        # check diagonal
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row-1, col+1
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    def backtracking(self, chessboard, n, row):
        # base case
        if row == n:
            temp_res = []
            for temp in chessboard:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            self.result.append(temp_res)
        for i in range(n):
            if self.isValid(chessboard, n, row, i):
                chessboard[row][i] = 'Q'
                self.backtracking(chessboard, n, row+1)
                chessboard[row][i] = '.'
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = [['.'] * n for _ in range(n)]
        self.backtracking(chessboard, n, 0)
        return self.result

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
