class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        m, n = len(sequence), len(word)
        if m < n: 
            return 0 

        f = [0] * m 
        i, j = n-1, 0
        while i < m:
            while j < n:  
                if sequence[i-n+j+1] != word[j]: 
                    break 
                j += 1 
            if j == n: 
                f[i] = f[max(i-n, 0)] + 1 
            j = 0 
            i += 1 

        return max(f)

if __name__ == "__main__": 
    s = Solution() 

    # sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    # word = "aaaba"
    # assert s.maxRepeating(sequence, word) == 5

    # sequence = "abab"
    # word = "ab"
    # assert s.maxRepeating(sequence, word) == 2 

    sequence = "ababc"
    word = "ab"
    assert s.maxRepeating(sequence, word) == 2 

