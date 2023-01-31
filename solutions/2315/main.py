class Solution:
    def countAsterisks(self, s: str) -> int:
        res = count = 0 
        first = None 
        for ch in s: 
            if ch == "*": 
                count += 1
            elif ch == "|": 
                if first is None: 
                    first = True 
                    res += count 
                    count = 0 
                else:
                    count = 0 
                    first = None 
        res += count 
        return res 
    
if __name__ == "__main__": 
    sol = Solution() 

    s = "l|*e*et|c**o|*de|"
    assert sol.countAsterisks(s) == 2 
