class Solution:
    def minimumLength(self, s: str) -> int:
        cur = s[0]
        n = len(s)
        i, j = 0, n-1 
        while i < j: 
            if s[j] != cur: 
                break 
            while i < j and s[i] == cur: 
                i += 1 
            if i == j: 
                return 0 
            while j > i and s[j] == cur: 
                j -= 1
            if i < j:  
                cur = s[i]
        return j-i+1 

if __name__ == "__main__": 
    sol = Solution() 

    # assert sol.minimumLength("aabccabba") == 3
    assert sol.minimumLength("cabaabac") == 0
    assert sol.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb") == 1