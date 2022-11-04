class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        sequence = list(sequence)
        repeat = max_repeat = 0 
        i = j = 0  
        while i < len(sequence): 
            if sequence[i] != word[j]:
                i += 1 
            while i < len(sequence) and j < len(word) and sequence[i] == word[j]: 
                j += 1 
                i += 1 
            if j == len(word): 
                repeat += 1 
                j = 0 
            else: 
                # NOTE, need to reset i 
                i -= j 
                j = 0 
                max_repeat = max(repeat, max_repeat)
                repeat = 0 
        max_repeat = max(repeat, max_repeat)
        return max_repeat 

if __name__ == "__main__": 
    s = Solution() 

    # cannot handle this case 
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    assert s.maxRepeating(sequence, word) == 5

    sequence = "abab"
    word = "ab"
    assert s.maxRepeating(sequence, word) == 2 

    sequence = "ababc"
    word = "ab"
    assert s.maxRepeating(sequence, word) == 2 

