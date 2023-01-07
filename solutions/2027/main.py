class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0 
        count = 0 
        for ch in s: 
            if ch == "X": 
                count += 1 
            else: 
                if count == 1:
                    count += 1 
                elif count > 0:  
                    res += 1 
                    count = 0 
            if count == 3: 
                res += 1 
                count = 0 
        if count > 0: 
            res += 1 
        return res 
            
if __name__ == "__main__": 
    sol = Solution() 

    assert sol.minimumMoves("OXOX") == 1 