from collections import Counter 
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        letter_to_idx = {
            "Q": 0, 
            "W": 1, 
            "E": 2, 
            "R": 3, 
        }
        idx_to_letter = {}
        for k, v in letter_to_idx.items(): 
            idx_to_letter[v] = k 

        total = Counter(s)
        outside = [0]*4
        for k, v in idx_to_letter.items(): 
            outside[k] = total[v]

        if max(outside) == n//4:
            return 0 

        i = j = 0 
        res = float("inf")
        while i < n and j < n: 
            while j < n and max(outside) > n//4: 
                outside[letter_to_idx[s[j]]] -= 1
                j += 1 
            while i < j and max(outside) <= n//4: 
                outside[letter_to_idx[s[i]]] += 1
                i += 1 
            res = min(res, j-i+1)
        
        return res  


if __name__ == "__main__": 
    sol = Solution() 

    s = "WWEQERQWQWWRWWERQWEQ"
    assert sol.balancedString(s) == 4 

    s = "WWQQRRRRQRQQ"
    assert sol.balancedString(s) == 4 

    # s = "QWER"
    # assert sol.balancedString(s) == 0

    # s = "QQWE"
    # assert sol.balancedString(s) == 1 