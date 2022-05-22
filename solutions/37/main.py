from typing import List

class Solution:
    @staticmethod
    def isValid(board, n, row, col, val):
        # check row
        for i in range(n):
            if board[row][i] == val:
                return False
        # check col
        for i in range(n):
            if board[i][col] == val:
                return False
        # check block
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        for i in range(startRow, startRow+3):
            for j in range(startCol, startCol+3):
                if board[i][j] == val:
                    return False
        return True
    def backtracking(self, board, n):
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    digit = str(k)
                    if self.isValid(board, n, i, j, digit):
                        board[i][j] = digit
                        if (self.backtracking(board, n)):
                            return True
                        board[i][j] = '.'
                return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board, len(board))

if __name__ == "__main__":
    s = Solution() 
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(board)
    print(board)
