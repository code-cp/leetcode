from typing import List 

class Solution:
    @staticmethod
    def checkWin(s):
        if s[0] == s[1] and s[1] == s[2]:
            if s[0] == 'X' or s[0] == 'O':
                return True
        return False

    @staticmethod
    def checkFull(board):
        for s in board:
            if s[0] == ' ' or s[1] == ' ' or s[2] == ' ':
                return False
        return True

    @staticmethod
    def checkEmpty(board):
        for s in board:
            if s[0] != ' ' or s[1] != ' ' or s[2] != ' ':
                return False
        return True

    def shouldEnd(self, board):
        # check if full
        if self.checkFull(board):
            return True
        # check if any player wins
        for i in range(3):
            if self.checkWin(board[i][0]+board[i][1]+board[i][2]):
                return True
            elif self.checkWin(board[0][i]+board[1][i]+board[2][i]):
                return True
        if self.checkWin(board[0][0]+board[1][1]+board[2][2]):
            return True
        elif self.checkWin(board[0][2]+board[1][1]+board[2][0]):
            return True
        return False

    def backtracking(self, board_temp, cPre, board):
        # base case
        if board_temp == board:
            return True
        elif self.shouldEnd(board_temp):
            return False

        # prune
        for i in range(3):
            for j in range(3):
                if board_temp[i][j] != ' ':
                    if board_temp[i][j] != board[i][j]:
                        return False

        if cPre == ' ' or cPre == 'O':
            cNext = 'X'
        elif cPre == 'X':
            cNext = 'O'
        cPre = cNext

        for i in range(3):
            for j in range(3):
                if board_temp[i][j] != ' ':
                    continue
                text = list(board_temp[i])
                text[j] = cNext
                board_temp[i] = "".join(text)
                if self.backtracking(board_temp, cPre, board):
                    return True
                text = list(board_temp[i])
                text[j] = ' '
                board_temp[i] = "".join(text)

        return False

    def validTicTacToe(self, board: List[str]) -> bool:
        if self.checkEmpty(board):
            return True
        board_temp = ["   " for _ in range(3)]
        return self.backtracking(board_temp, ' ', board)

if __name__ == "__main__":
    board = ["XOX","O O","XOX"]
    s = Solution()
    assert s.validTicTacToe(board) 
