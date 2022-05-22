from typing import * 

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moves = [0] * 2
        start = -1 
        for i in range(1, len(colors)): 
            if colors[i] == colors[i-1]: 
                if start == -1: 
                    start = 2
                else: 
                    start += 1 
            if colors[i] != colors[i-1] or i == len(colors)-1: 
                if colors[i-1] == "A": 
                    moves[0] += max(start-2, 0) 
                else: 
                    moves[1] += max(start-2, 0)
                start = -1
        return moves[0] > moves[1]
        
if __name__ == "__main__": 
    s = Solution()

    colors = "AAABABB"
    assert s.winnerOfGame(colors)

    colors = "ABBBBBBBAAA"
    assert not s.winnerOfGame(colors)

    colors = "AABB"
    assert not s.winnerOfGame(colors)

    colors = "AAABABB"
    assert s.winnerOfGame(colors)

    colors = "AAAABBBB"
    assert not s.winnerOfGame(colors)