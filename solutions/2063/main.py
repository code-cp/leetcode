from typing import List 

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # dp table
        dp = [0] * len(word)
        # initialize
        dp[0] = 1 if word[0] in vowels else 0
        # traverse dp table
        for i in range(1, len(word)):
            if word[i] in vowels:
                dp[i] = dp[i-1]+i+1
            else:
                dp[i] = dp[i-1]
        return sum(dp)

if __name__ == "__main__": 
    word = "noosabasboosa"
    s = Solution()
    assert s.countVowels(word) == 237
