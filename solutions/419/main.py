from typing import List 

class Solution:
    def dfs(self, board, i, j):
        # base case
        if i >= len(board) or i < 0:
            return
        if j >= len(board[0]) or j < 0:
            return
        if board[i][j] == ".":
            return
        board[i][j] = "."
        # traverse
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)
    def countBattleships(self, board: List[List[str]]) -> int:
        result = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    result += 1
                    self.dfs(board, i, j)
        return result

if __name__ == "__main__": 
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    s = Solution()
    assert s.countBattleships(board) == 2 
