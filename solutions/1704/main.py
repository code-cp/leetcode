class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        is_vowel = lambda ch: True if ch.lower() in ['a','e','i','o','u'] else False 
        n = len(s)
        first = s[:n//2]
        second = s[n//2:]
        first = [ch for ch in first if is_vowel(ch)]
        second = [ch for ch in second if is_vowel(ch)]
        return len(first) == len(second)
