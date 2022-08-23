from typing import * 

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # corners of every rectangle should be 0000, 1111 or 0011
        for r in range(n): 
            for c in range(n):
                if board[0][0] ^ board[r][0] ^ board[r][c] ^ board[0][c]:
                    return -1
        # traverse board 
        rowSum = colSum = rowSwap = colSwap = 0  
        for i in range(n):
            rowSum += board[0][i]
            colSum += board[i][0]
            rowSwap += (board[i][0] == i%2)
            colSwap += (board[0][i] == i%2)
        # check number of 0, 1 
        if rowSum != n//2 and rowSum != (n+1)//2:
            return -1 
        if colSum != n//2 and colSum != (n+1)//2:
            return -1 
        # check min step based on n even or odd
        if n % 2: 
            if colSwap % 2:
                colSwap = n - colSwap
            if rowSwap % 2: 
                rowSwap = n - rowSwap
        else: 
            colSwap = min(n - colSwap, colSwap)
            rowSwap = min(n - rowSwap, rowSwap)
        # /2 since we fix 2 nums at each step 
        return (rowSwap + colSwap) // 2  
 
if __name__ == "__main__": 
    s = Solution()

    board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    assert s.movesToChessboard(board) == 2 