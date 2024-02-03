from typing import * 

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # dp[i][cur_pos] means at i iteration 
        # put cur pos to 12 clock 
        # what is the min. turn count 
        # dp[i][cur_pos] = key[i]
        # dp[i-1][prev_pos] = key[i-1]
        # dp[i][cur_pos] = dp[i-1][prev_pos] + min(abs(prev_pos - cur_pos), ring_size - abs(prev_pos - cur_pos))
                
        n = len(key)
        m = len(ring)
        dp = [[float("inf")] * m for _ in range(n)]
        
        letter_to_pos = {}
        for i in range(m):
            # NOTE, same char can appear at different positions 
            letter_to_pos.setdefault(ring[i], []).append(i)
        
        # Initially, the first character of the ring is aligned at the "12:00" direction
        # we need to diag key[0] to 12 clock 
        for cur_pos in letter_to_pos[key[0]]:
            # diag clock wise or ccw, see which distance is smaller 
            dp[0][cur_pos] = min(cur_pos, m - cur_pos)
        
        for i in range(1, n): 
            for cur_pos in letter_to_pos[key[i]]:
                for prev_pos in letter_to_pos[key[i-1]]:
                    diff = abs(prev_pos - cur_pos)
                    dp[i][cur_pos] = min(
                        dp[i][cur_pos], 
                        dp[i-1][prev_pos] + 
                        min(diff, m-diff)
                    )
                
        res = float("inf")
        # any of the last char can be the end position 
        for pos in letter_to_pos[key[-1]]:
            res = min(res, dp[-1][pos])
        
        # each diag is also a count, so +n 
        return res + n 
        
        