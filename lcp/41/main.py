from typing import * 
from collections import deque 

# backtracking
class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        max_cnt = 0 
        m, n = len(chessboard), len(chessboard[0])
        
        def checkValid(i, j):
            nonlocal m 
            nonlocal n 
            if i < 0 or i >= m: 
                return False  
            if j < 0 or j >= n: 
                return False 
            return True 
        
        def countFlip(i, j): 
            nonlocal m 
            nonlocal n 
            nonlocal chessboard
            nonlocal blacks 
            
            # count all whites 
            whites = {}
            for di in range(-1,2): 
                for dj in range(-1,2): 
                    whites[(di,dj)] = []
                    r, c = i+di, j+dj
                    while checkValid(r, c): 
                        if blacks[r][c] == 1: 
                            break 
                        if chessboard[r][c] == ".": 
                            break 
                        if chessboard[r][c] == "O":
                            whites[(di,dj)].append((r,c))
                        r, c = r+di, c+dj

            # check whites surrounded by blacks 
            cnt = 0 
            new_blacks = set()
            for k, v in whites.items(): 
                if len(v) == 0: 
                    continue 
                vi, vj = v[-1]
                r, c = vi+k[0], vj+k[1]
                if not checkValid(r,c): 
                    continue 
                if blacks[r][c] == 0:
                    continue  
                cnt += len(v)
                for (vi,vj) in v: 
                    # mark new whites as black 
                    # NOTE, this will affect the later iterations 
                    blacks[vi][vj] = 1 
                    # print(f"countFlip {vi} {vj}")
                    new_blacks.add((vi,vj))

            return cnt, new_blacks 
        
        blacks = [[0]*n for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                if chessboard[i][j] == "X": 
                    blacks[i][j] = 1 
        
        for i in range(m): 
            for j in range(n): 
                if chessboard[i][j] != ".": 
                    continue 
                blacks[i][j] = 1 
                all_changed = set()
                total = 0 
                cnt, new_blacks = countFlip(i, j)
                total += cnt 
                while len(new_blacks) > 0:
                    for (ni,nj) in new_blacks: 
                        # NOTE, this line is useless 
                        # blacks[ni][nj] = 1
                        # print(f"while {ni} {nj}")
                        all_changed.add((ni,nj))
                    cur_changed = set()
                    for (ni,nj) in new_blacks:
                        # NOTE, need to set black in countFlip
                        # otherwise it will double count here 
                        cnt, nb = countFlip(ni,nj)
                        total += cnt 
                        for (ni,nj) in nb: 
                            cur_changed.add((ni,nj))
                    new_blacks = cur_changed
                # backtrack 
                blacks[i][j] = 0
                for (ai,aj) in all_changed: 
                    blacks[ai][aj] = 0 
                max_cnt = max(total, max_cnt)
                
        return max_cnt
    
if __name__ == "__main__": 
    s = Solution() 

    assert s.flipChess(["......","......","XOOO..","..OOOX","...XX.","......","......"]) == 6    
    # assert s.flipChess([".X.",".O.","XO."]) == 2
    # assert s.flipChess(["....X.","....X.","XOOO..","......","......"]) == 3
    # place at center to get max. whites 
    # assert s.flipChess([".O.....",".O.....","XOO.OOX",".OO.OO.",".XO.OX.","..X.X.."]) == 10