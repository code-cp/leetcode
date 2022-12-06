from collections import Counter 
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        atos = lambda w: w if not w.isalpha() else " "
        word = [atos(w) for w in word]
        word = "".join(word)
        word = word.split()
        word = [int(w) for w in word]
        cnt = Counter(word)
        return len(cnt) 

if __name__ == "__main__": 
    s = Solution() 

    word = "a123bc34d8ef34"
    assert s.numDifferentIntegers(word) == 3 