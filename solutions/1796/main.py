class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1 
        for ch in s: 
            if ch.isdigit(): 
                n = int(ch)
                if n > first:
                    second = first   
                    first = n
                elif n != first and n > second: 
                    second = n 
        return second 

if __name__ == "__main__": 
    sol = Solution()

    s = "sjhtz8344"
    assert sol.secondHighest(s) == 4 