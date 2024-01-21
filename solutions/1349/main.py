from typing import * 

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        # dp[i][state1] = max(dp[i-1][state2] + count(dp[i][state1])) 
        # state1, state2 do not conflict 
        
        m, n = len(seats), len(seats[0])
        
        def checkSelf(row, state): 
            nonlocal n 
            cur = seats[row]
            chairs = 0 
            # check chairs 
            # NOTE, bits are from right to left 
            for i in range(n-1, -1, -1): 
                if cur[i] == "#": 
                    chairs |= (1 << (n-1-i))
            if (state & chairs) > 0: 
                return False 
            
            # check neighbours 
            # NOTE, only need to check right seat 
            for i in range(n-1): 
                c1 = (state >> i) & 1 
                if i == 0: 
                    if n > 1: 
                        c2 = (state >> (i+1)) & 1 
                        if c1 & c2 > 0: 
                            return False 
                        continue 
                    else: 
                        return True 
                c2 = (state >> (i+1)) & 1 
                if c1 & c2 > 0: 
                    return False 
            return True 
            
        def checkPrev(cur, prev):
            nonlocal n 
            for i in range(n): 
                p = (prev >> i) & 1
                # only check chairs that are taken  
                if p == 0: 
                    continue
                 
                if i == 0: 
                    if n == 1: 
                        return True 
                    else: 
                        c2 = (cur >> 1) & 1 
                        if p & c2 > 0: 
                            return False 
                        continue 
                if i == n-1:
                    if n == 2: 
                        return True 
                    else: 
                        c1 = (cur >> (n-2)) & 1 
                        if p & c1 > 0: 
                            return False 
                        continue 
                c1 = (cur >> (i-1)) & 1 
                c2 = (cur >> (i+1)) & 1 
                if p & c1 > 0 or p & c2 > 0: 
                    return False 
            return True 
        
        def countState(state):
            num = 0  
            while state > 0:
                state = state & (state - 1)
                num += 1  
            return num 
        
        dp = [[-1 for _ in range(1 << n)] for _ in range(m)]
        for state in range(1 << n): 
            if not checkSelf(0, state):
                continue  
            dp[0][state] = countState(state)
            
        for row in range(1, m): 
            for state in range(1 << n): 
                if not checkSelf(row, state):
                    # NOTE, if state is invalid, value should be -1, not 0 
                    dp[row][state] = -1  
                    continue 
                cur = countState(state)
                max_num = 0
                for prev in range(1 << n): 
                    if dp[row-1][prev] == -1: 
                        continue 
                    if not checkPrev(prev, state):
                        continue 
                    max_num = max(dp[row-1][prev] + cur, max_num)
                dp[row][state] = max_num 
                
        return max(dp[m-1])
    
if __name__ == "__main__": 
    s = Solution() 
    
    # seats = [["#",".","#","#",".","#"],
    #          [".","#","#","#","#","."],
    #          ["#",".","#","#",".","#"]]
    # assert s.maxStudents(seats) == 4 

    # seats = [["#",".","."],
    #          [".","#","."]]
    # assert s.maxStudents(seats) == 3 

    seats = [["#",".",".",".","#"],
             [".","#",".","#","."],
             [".",".","#",".","."],
             [".","#",".","#","."],
             ["#",".",".",".","#"]]
    assert s.maxStudents(seats) == 10 
            
            
                
        