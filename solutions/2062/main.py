from typing import List 

class Solution:
    @staticmethod
    def checkCount(count):
        for c in count:
            if c == 0:
                return False
        return True
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        count = [0] * 5
        valid = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(word)):
            if word[i] not in valid:
                continue
            count[valid.index(word[i])] += 1
            j = i + 1
            while j < len(word) and word[j] in valid:
                count[valid.index(word[j])] += 1
                j += 1
                if self.checkCount(count):
                    result += 1
            # reset
            count = [0] * 5
        return result

if __name__ == "__main__": 
    word = "cuaieuouac"
    s = Solution()
    assert s.countVowelSubstrings(word) == 7
